'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName))
                    
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        [self.visit(i, c) for i in ast.decl]
        return c

    def visitClassDecl(self, ast:ClassDecl, c):
        """
        classname: Id
        memlist: List[MemDecl]
        parentname: Id = None  # None if there is no parent
        """
        self.className = ast.classname.name
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        if not ast.parentname:
            self.isHaveParent = False
            self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        else:
            self.isHaveParent = True
            self.emit.printout(
                self.emit.emitPROLOG(self.className, ast.parentname.name)
            )
        self.cast = ast
        isHaveCon = False
        for x in ast.memlist:
            self.visit(x, 0)
            if type(x) is MethodDecl and x.name.name == "Constructor":
                isHaveCon = True
        # generate default constructor
        if not isHaveCon:
            self.genMETHOD(
                MethodDecl(Instance(), Id("<init>"), list(), Block([])),
                self.env,
                Frame("<init>", VoidType()),
            )
        self.genMETHOD(
            MethodDecl(Static(), Id("<clinit>"), list(), Block([])),
            self.env,
            Frame("<clinit>", VoidType()),
        )

        [self.visit(ele, SubBody(None, self.env)) for ele in ast.memlist if type(ele) is MethodDecl]
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl:MethodDecl, o, frame):
        isInit = consdecl.name.name == "<init>"
        isClassInit = consdecl.name.name == "<clinit>"
        isMain = (
                consdecl.name.name == "main"
                and len(consdecl.param) == 0
        )
        returnType = VoidType() if isInit or isClassInit else VoidType()
        methodName = "<init>" if isInit else consdecl.name.name
        methodName = "<clinit>" if isClassInit else methodName

        intype = (
            [ArrayType(0, StringType())]
            if isMain
            else list(map(lambda x: x.varType, consdecl.param))
        )

        mtype = MType(intype, returnType)
        if isInit:
            self.contype = mtype
        body = consdecl.body

        isStatic = True if isinstance(consdecl.kind, Static) else False
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, isStatic, frame))

        frame.enterScope(True)

        glenv = o
        lcenv = []
        e = SubBody(frame, lcenv)
        penv = []
        p = SubBody(frame, penv)
        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    "this",
                    ClassType(Id(self.className)),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame,
                )
            )
            for x in consdecl.param:
                p = self.visit(x, p)
        elif isMain:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    "args",
                    ArrayType(0, StringType()),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame,
                )
            )

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(
                self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame)
            )

            if not self.isHaveParent:
                self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            else:
                self.emit.printout(
                    self.emit.emitINVOKESPECIAL(frame, self.cast.parentname.name + "/<init>", self.contype))

            for x in self.cast.memlist:
                if type(x) is AttributeDecl and type(x.kind) == Instance:
                    if isinstance(x.decl, VarDecl) and x.decl.varInit:
                        self.emit.printout(
                            self.emit.emitREADVAR(
                                "this", ClassType(Id(self.className)), 0, frame
                            )
                        )
                        self.emit.printout(self.visit(x, frame))
        elif isClassInit:
            for x in self.cast.memlist:
                if type(x) is AttributeDecl and type(x.kind) is Static:
                    if isinstance(x.decl, VarDecl) and x.decl.varInit:
                        self.emit.printout(self.visit(x, frame))
        elif type(consdecl.kind) is Instance:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    "this",
                    ClassType(Id(self.className)),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame,
                )
            )
            for x in consdecl.param:
                p = self.visit(x, p)
        elif type(consdecl.kind) is Static:
            for x in consdecl.param:
                p = self.visit(x, p)

        list(
            map(
                lambda x: self.visit(x, SubBody(frame, p.sym + e.sym + glenv)),
                body.inst,
            )
        )
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

        frame.exitScope()



    def visitMethodDecl(self, ast: MethodDecl, o):

        if o == 0 or o == 3:
            return Symbol(
                ast.name.name,
                MType([x.varType for x in ast.param], VoidType()),
                CName(self.className),
            )

        frame = Frame(ast.name.name, VoidType())
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(
            ast.name.name,
            MType([x.varType for x in ast.param], VoidType()),
            CName(self.className),
        )

    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    
