
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from StaticError import *

class Utils:
    def lookup(self,sym,lst,func):
        for x in lst:
            if sym.name == func(x):
                if type(sym.mtype) is not type(x.mtype):
                    if type(sym.mtype) is MType or type(x.mtype) is MType:
                        continue
                return x
        return None



class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return "Mtype: {}, {}".format(self.partype, self.rettype)


class Symbol:
    def __init__(self,name,mtype,value = None, isVar = 0, isInst = True, isDefault = False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.isVar = isVar
        self.isInst = isInst
        self.isDefault = isDefault

    def __str__(self):
        return "Symbol: {}, {}, {} ".format(self.name, str(self.mtype), self.value)



class StaticChecker(BaseVisitor, Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
    glob = {}
    current_class = None
    current_method = None
    loop_lst = []
    def __init__(self,ast):
        self.ast = ast

    def check_type(self, left, right, x, flag=-1):
        if type(left) is not type(right):
            if type(left) is IntType:
                raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
            elif type(left) is StringType:
                raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
            elif type(left) is FloatType:
                if type(right) is not IntType:
                    raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
            elif type(left) is BoolType:
                raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
            elif type(left) is ArrayType:
                raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
            elif type(left) is ClassType:
                if right is not None:
                    raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
        else:
            if type(left) is ClassType and type(right) is ClassType:
                if left.classname.name != right.classname.name:
                    raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
            while type(left) is ArrayType:
                if left.size != right.size:
                    raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
                else:
                    if type(left.eleType) is not type(right.eleType):
                        if type(left.eleType) is IntType:
                            raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
                        elif type(left.eleType) is StringType:
                            raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
                        elif type(left.eleType) is FloatType:
                            if type(right.eleType) is not IntType:
                                raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
                        elif type(left.eleType) is BoolType:
                            raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
                        elif type(left.eleType) is ArrayType:
                            raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
                        elif type(left.eleType) is ClassType:
                            if right is not None:
                                raise TypeMismatchInConstant(x) if flag == 1 else TypeMismatchInStatement(x) if flag==-1 else TypeMismatchInExpression(x)
                    left = left.eleType
                    right = right.eleType



    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def checkRedeclared(self, sym, kind, c):
        if self.lookup(sym, c, lambda x: x.name):
            raise Redeclared(kind, sym.name)
        return sym



    def visitProgram(self,ast, c):
        """
        decl: List[ClassDecl]
        """
        self.glob = {}
        self.current_class = None
        self.current_method = None
        self.loop_lst = []
        cc = c.copy()
        haveEntry = False
        for x in ast.decl:
            self.current_class = x.classname.name
            if self.visitClassDecl(x, cc):
                haveEntry = True
            if x.classname.name == "Program":
                if not haveEntry:
                    raise NoEntryPoint()

        if not haveEntry:
            raise NoEntryPoint()

        return []


    def visitClassDecl(self, ast, c):
        """
        classname: Id
        memlist: List[MemDecl]
        parentname: Id = None  # None if there is no parent
        """
        sym = Symbol(ast.classname.name, ClassType(ast.classname.name))
        kind = Class()
        c.append(self.checkRedeclared(sym, kind, c))
        haveEntry = False
        local_envi = []
        inherit_envi = []
        if ast.parentname:
            if ast.parentname.name not in self.glob.keys():
                raise Undeclared(Class(), ast.parentname.name)
            inherit_envi = self.glob[ast.parentname.name]
        local_envi.append(Symbol("Constructor", MType([], VoidType()), isInst=True, isDefault=True))
        local_envi.append(Symbol("Destructor", MType([], VoidType()), isInst=True, isDefault=True))

        for x in ast.memlist:
            self.glob[ast.classname.name] = local_envi
            if type(x) is MethodDecl:
                self.current_method = x.name.name
                if x.name.name == "main" and x.param == [] and ast.classname.name == "Program":
                    haveEntry = True
                    self.visitMethodDecl(x, local_envi, inherit_envi.copy())
                elif x.name.name == "Constructor":
                    idx = -1
                    for i in range(len(local_envi)):
                        if local_envi[i].name == "Constructor" and local_envi[i].isDefault:
                            idx = i
                            break
                    if len(local_envi) != 0 and idx != -1:
                        local_envi.pop(idx)
                    self.visitMethodDecl(x, local_envi, inherit_envi.copy())
                elif x.name.name == "Destructor":
                    idx = -1
                    for i in range(len(local_envi)):
                        if local_envi[i].name == "Destructor" and local_envi[i].isDefault:
                            idx = i
                            break
                    if len(local_envi) != 0 and idx != -1:
                        local_envi.pop(idx)
                    self.visitMethodDecl(x, local_envi, inherit_envi.copy())
                else:
                    self.visitMethodDecl(x, local_envi, inherit_envi.copy())
            else:
                self.visitAttributeDecl(x, local_envi, inherit_envi)


        self.glob[ast.classname.name] = local_envi
        return haveEntry




    def visitMethodDecl(self,ast, c, inherit_envi):
        """
        class MethodDecl(MemDecl):
            kind: SIKind
            name: Id
            param: List[VarDecl]
            body: Block
        """
        void = VoidType()
        symbol = Symbol(ast.name.name, MType([i.varType for i in ast.param], void), isInst=True if isinstance(ast.kind, Instance) else False, isVar=0)
        kind = Method()
        c.append(self.checkRedeclared(symbol, kind, c))
        local_envi = []
        for i in ast.param:
            local_envi.append(self.checkRedeclared(Symbol(i.variable.name, i.varType, isVar=1),Parameter(),local_envi))
            idx = -1
            for x in range(len(inherit_envi)):
                if i.variable.name == inherit_envi[x].name:
                    idx = x
                    break
            if len(inherit_envi) != 0 and idx != -1:
                inherit_envi.pop(idx)
        lst = []
        self.visitBlock(ast.body, lst, inherit_envi, param_envi=local_envi+[c[-1]])




    def visitBlock(self, ast, c, inherit_envi, param_envi = []):
        """
        class Block(Stmt):
            inst: List[Inst]
        """

        local_envi = param_envi

        for x in ast.inst:
            if type(x) is Return:
                if self.current_method == "Constructor" and x.expr is not None:
                    raise TypeMismatchInStatement(x)
                if self.current_method == "Destructor" and x.expr is not None:
                    raise TypeMismatchInStatement(x)
                if self.current_method == "main" and self.current_class == "Program" and x.expr is not None:
                    raise TypeMismatchInStatement(x)
                ret_val, ret_typ, isVar = self.visit(x, local_envi + c + inherit_envi)
                for i in c+param_envi:
                    if i.name == self.current_method:
                        if not isinstance(i.mtype, MType):
                            continue
                        if isinstance(i.mtype.rettype, VoidType):
                            i.mtype.rettype = ret_typ
                            i.value = ret_val
                            i.isVar = isVar
                        else:
                            if type(i.mtype.rettype) is not type(ret_typ):
                                raise TypeMismatchInStatement(x)
                        break

            elif type(x) is Assign:
                rhs_val, rhs_typ, _ = self.visit(x.exp, local_envi + c + inherit_envi)
                if type(x.lhs) is Id:
                    lst = local_envi + c + inherit_envi
                    flag = False
                    for i in lst:
                        if i.name == x.lhs.name:
                            if type(i.mtype) is VoidType:
                                raise TypeMismatchInStatement(x)
                            flag = True
                            if i.isVar == 1:
                                val, typ, _ = self.visit(x.exp, lst)
                                self.check_type(i.mtype, typ, x)
                                break
                            elif i.isVar == -1:
                                raise CannotAssignToConstant(x)
                    if not flag:
                        raise Undeclared(Identifier(), x.lhs.name)
                else:
                    lhs_val, lhs_typ, isVar = self.visit(x.lhs, local_envi + c + inherit_envi)
                    if isVar == -1:
                        raise CannotAssignToConstant(x)
                    if type(lhs_typ) is VoidType:
                        raise TypeMismatchInStatement(x)
                    self.check_type(lhs_typ, rhs_typ, x)

            elif type(x) is For:
                self.visitFor(x, local_envi + c, inherit_envi.copy())
            elif type(x) is If:
                self.visitIf(x, local_envi + c, inherit_envi.copy())
            elif type(x) is CallStmt:
                self.visitCallStmt(x, local_envi + c + inherit_envi)
            elif type(x) is Break:
                if not self.loop_lst:
                    raise MustInLoop(x)
            elif type(x) is Continue:
                if not self.loop_lst:
                    raise MustInLoop(x)
            elif type(x) is VarDecl:
                symbol = Symbol(x.variable.name, x.varType, isVar=1, isInst=True)
                kind = Variable()
                local_envi.append(self.checkRedeclared(symbol, kind, local_envi))
                if isinstance(x.varType, ClassType):
                    if x.varType.classname.name not in self.glob.keys():
                        raise Undeclared(Class(), x.varType.classname.name)
                value = None
                if x.varInit:
                    value, typ, isVar = self.visit(x.varInit, local_envi + c + inherit_envi)
                    self.check_type(x.varType, typ, x)
                local_envi[-1].value = value
                idx = -1
                for i in range(len(inherit_envi)):
                    if x.variable.name == inherit_envi[i].name:
                        idx = i
                        break
                if len(inherit_envi) != 0 and idx != -1:
                    inherit_envi.pop(idx)
            elif type(x) is ConstDecl:

                symbol = Symbol(x.constant.name, x.constType, isVar=-1, isInst=True)
                kind = Constant()
                local_envi.append(self.checkRedeclared(symbol, kind, local_envi))
                if isinstance(x.constType, ClassType):
                    if x.constType.classname.name not in self.glob.keys():
                        raise Undeclared(Class(), x.constType.classname.name)
                value = None
                if x.value:
                    value, typ, isVar = self.visit(x.value, local_envi + c + inherit_envi)
                    if isVar == 1:
                        raise IllegalConstantExpression(x.value)
                    self.check_type(x.constType, typ, x, 1)
                else:
                    raise IllegalConstantExpression(None)
                local_envi[-1].value = value
                idx = -1
                for i in range(len(inherit_envi)):
                    if x.constant.name == inherit_envi[i].name:
                        idx = i
                        break
                if len(inherit_envi) != 0 and idx != -1:
                    inherit_envi.pop(idx)
            elif type(x) is Block:
                self.visitBlock(x, local_envi + c, inherit_envi, param_envi=[])


    def visitReturn(self, ast, c):
        """
        class Return(Stmt):
            expr: Expr = None
        """
        if ast.expr:
            return self.visit(ast.expr, c)
        else:
            isVar = 0
            return None, VoidType(), isVar



    def visitAttributeDecl(self, ast, c, inherit_envi):
        """
        class AttributeDecl(MemDecl):
            kind: SIKind  # Instance or Static
            decl: StoreDecl  # VarDecl for mutable or ConstDecl for immutable
        """
        if type(ast.decl) is VarDecl:
            idx = -1
            for i in range(len(inherit_envi)):
                if ast.decl.variable.name == inherit_envi[i].name:
                    idx = i
                    break
            if len(inherit_envi) != 0 and idx != -1:
                inherit_envi.pop(idx)

            symbol = Symbol(ast.decl.variable.name, ast.decl.varType, isVar=1, isInst=True if isinstance(ast.kind, Instance) else False)
            kind = Attribute()
            c.append(self.checkRedeclared(symbol, kind, c))
            if isinstance(ast.decl.varType, ClassType):
                if ast.decl.varType.classname.name not in self.glob.keys():
                    raise Undeclared(Class(), ast.decl.varType.classname.name)
            value = None
            if ast.decl.varInit:
                val, typ, isVar = self.visit(ast.decl.varInit, inherit_envi)
                self.check_type(ast.decl.varType, typ, ast.decl)
                c[-1].value = val
        else:
            idx = -1
            for i in range(len(inherit_envi)):
                if ast.decl.constant.name == inherit_envi[i].name:
                    idx = i
                    break
            if len(inherit_envi) != 0 and idx != -1:
                inherit_envi.pop(idx)
            symbol = Symbol(ast.decl.constant.name, ast.decl.constType, isVar=-1, isInst=True if isinstance(ast.kind, Instance) else False)
            kind = Attribute()
            c.append(self.checkRedeclared(symbol, kind, c))
            if isinstance(ast.decl.constType, ClassType):
                if ast.decl.constType.classname.name not in self.glob.keys():
                    raise Undeclared(Class(), ast.decl.constType.classname.name)
            value = None
            if ast.decl.value:
                val, typ, isVar = self.visit(ast.decl.value, inherit_envi)
                if isVar == 1:
                    raise IllegalConstantExpression(ast.decl.value)
                self.check_type(ast.decl.constType, typ, ast.decl, 1)
                c[-1].value = val
            else:
                raise IllegalConstantExpression(None)


    def visitId(self, ast, c):
        for i in c:
            if ast.name == i.name:
                return i.value, i.mtype, i.isVar
        raise Undeclared(Identifier(), ast.name)

    def visitNewExpr(self, ast, c):
        """
        class NewExpr(Expr):
            classname: Id
            param: List[Expr]
        """
        if ast.classname.name not in self.glob.keys():
            raise Undeclared(Class(), ast.classname.name)
        cons_typ = None
        for i in self.glob[ast.classname.name]:
            if i.name == "Constructor":
                cons_typ = i.mtype
                break
        param_lst = [self.visit(i, c)[1] for i in ast.param]
        if len(param_lst) != len(cons_typ.partype):
            raise TypeMismatchInExpression(ast)
        for i in range(len(param_lst)):
            self.check_type(param_lst[i], cons_typ.partype[i], ast, flag=0)
        return None, ClassType(ast.classname), 0

    def visitFieldAccess(self, ast, c):
        """
        class FieldAccess(LHS):
            obj: Expr
            fieldname: Id
        """
        val = None
        typ = None
        if type(ast.obj) is Id:
            flag = False
            for i in c:
                if ast.obj.name == i.name:
                    val, typ = i.value, i.mtype
                    flag = True
                    break
            if not flag:
                if ast.obj.name not in self.glob.keys():
                    raise Undeclared(Identifier(), ast.obj.name)
                else:
                    local_envi = self.glob[ast.obj.name]
                    for i in local_envi:
                        if i.name == ast.fieldname.name:
                            if i.isInst:
                                raise IllegalMemberAccess(ast)
                            else:
                                if type(i.mtype) is MType:
                                    continue
                                return i.value, i.mtype, i.isVar
                    raise Undeclared(Attribute(), ast.fieldname.name)
        else:
            val, typ, _ = self.visit(ast.obj, c)
        local_envi = []
        if type(typ) is not ClassType:
            if isinstance(ast.obj, Id) and ast.obj.name in self.glob.keys():
                local_envi = self.glob[ast.obj.name]
            else:
                raise TypeMismatchInExpression(ast)
        else:
            local_envi = self.glob[typ.classname.name]
        dump = False
        for i in local_envi:
            if i.name == ast.fieldname.name:
                if not isinstance(typ, ClassType):
                    dump = True
                if not (i.isInst or dump) or (i.isInst and dump):
                    raise IllegalMemberAccess(ast)
                else:
                    if type(i.mtype) is MType:
                        continue
                    return i.value, i.mtype, i.isVar
        raise Undeclared(Attribute(), ast.fieldname.name)

    def visitCallExpr(self, ast, c): 
        """
        class CallExpr(Expr):
            obj: Expr
            method: Id
            param: List[Expr]
        """
        val = None
        typ = None
        if type(ast.obj) is Id:
            flag = False
            for i in c:
                if ast.obj.name == i.name:
                    val, typ = i.value, i.mtype
                    flag = True
                    break
            if not flag:
                if ast.obj.name not in self.glob.keys():
                    raise Undeclared(Identifier(), ast.obj.name)
                else:
                    local_envi = self.glob[ast.obj.name]
                    func_val = func_typ = isVar = None
                    flag = False
                    for i in local_envi:
                        if i.name == ast.method.name and type(i.mtype) is MType:
                            if i.isInst:
                                raise IllegalMemberAccess(ast)
                            func_val, func_typ, isVar = i.value, i.mtype, i.isVar
                            flag = True
                            break
                    if not flag:
                        raise Undeclared(Method(), ast.method.name)
                    if type(func_typ) is not MType:
                        raise TypeMismatchInExpression(ast)
                    if type(func_typ.rettype) is VoidType:
                        raise TypeMismatchInExpression(ast)
                    partype_lst = func_typ.partype
                    param_lst = [self.visit(i, c)[1] for i in ast.param]
                    if len(partype_lst) != len(param_lst):
                        raise TypeMismatchInExpression(ast)
                    for i in range(len(param_lst)):
                        self.check_type(partype_lst[i], param_lst[i], ast, flag=0)
                    return None, func_typ.rettype, isVar
        else:
            val, typ, _ = self.visit(ast.obj, c)
        if type(typ) is not ClassType:
            raise TypeMismatchInExpression(ast)
        local_envi = self.glob[typ.classname.name]
        func_val = func_typ = isVar = None
        flag = False
        for i in local_envi:
            if i.name == ast.method.name and type(i.mtype) is MType:
                if not i.isInst:
                    raise IllegalMemberAccess(ast)
                func_val, func_typ, isVar = i.value, i.mtype, i.isVar
                flag = True
                break
        if not flag:
            raise Undeclared(Method(), ast.method.name)

        if type(func_typ) is not MType:
            raise TypeMismatchInExpression(ast)

        if type(func_typ.rettype) is VoidType:
            raise TypeMismatchInExpression(ast)
        partype_lst = func_typ.partype
        param_lst = [self.visit(i, c)[1] for i in ast.param]

        if len(partype_lst) != len(param_lst):
            raise TypeMismatchInExpression(ast)
        for i in range(len(param_lst)):
            self.check_type(partype_lst[i], param_lst[i], ast, flag=0)
        return None, func_typ.rettype, isVar


    def visitFor(self, ast, c, inherit_envi):
        """
        class For(Stmt):
            id: Id
            expr1: Expr
            expr2: Expr
            loop: Stmt
            expr3: Expr = None
        """
        self.loop_lst.append(ast)
        ret_val, _, _ = self.visit(ast.id, c)
        for i in c:
            if i.name == ast.id.name:
                if i.isVar == -1:
                    raise CannotAssignToConstant(Assign(ast.id, ast.expr1))
                break
        exp1_val, exp1_typ, _ = self.visit(ast.expr1, c)
        exp2_val, exp2_typ, _ = self.visit(ast.expr2, c)
        exp3_val, exp3_typ, _ = self.visit(ast.expr3, c)
        if type(exp1_typ) is not IntType or type(exp2_typ) is not IntType or type(exp3_typ) is not IntType:
            raise TypeMismatchInStatement(ast)
        if type(ast.loop) is Block:
            self.visitBlock(ast.loop, c, inherit_envi, param_envi=[])
        else:
            self.visit(ast.loop, c)
        self.loop_lst.pop()
    def visitIf(self, ast, c, inherit_envi):
        """
        class If(Stmt):
            expr: Expr
            thenStmt: Stmt
            elseStmt: Stmt = None  # None if there is no else branch
        """
        _, ret_typ, _ = self.visit(ast.expr, c)
        if type(ret_typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        if type(ast.thenStmt) is Block:
            self.visitBlock(ast.thenStmt, c, inherit_envi, param_envi=[])
        else:
            self.visit(ast.thenStmt, c)
        if ast.elseStmt:
            if type(ast.elseStmt) is Block:
                self.visitBlock(ast.elseStmt, c, inherit_envi, param_envi=[])
            elif type(ast.elseStmt) is If:
                self.visitIf(ast.elseStmt, c, inherit_envi.copy())
            else:
                self.visit(ast.elseStmt, c)

    def visitCallStmt(self, ast, c):
        """
        class CallStmt(Stmt):
            obj: Expr
            method: Id
            param: List[Expr]
        """
        val = None
        typ = None

        if type(ast.obj) is Id:
            flag = False
            for i in c:
                if ast.obj.name == i.name:
                    val, typ = i.value, i.mtype
                    flag = True
                    break
            if not flag:
                if ast.obj.name not in self.glob.keys():
                    raise Undeclared(Identifier(), ast.obj.name)
                else:
                    local_envi = self.glob[ast.obj.name]
                    func_val = func_typ = None
                    flag = False
                    for i in local_envi:
                        if i.name == ast.method.name and type(i.mtype) is MType:
                            if i.isInst:
                                raise IllegalMemberAccess(ast)
                            func_val, func_typ = i.value, i.mtype
                            flag = True
                            break
                    if not flag:
                        raise Undeclared(Method(), ast.method.name)

                    if type(func_typ) is not MType:
                        raise TypeMismatchInStatement(ast)
                    if type(func_typ.rettype) is not VoidType:
                        raise TypeMismatchInStatement(ast)
                    partype_lst = func_typ.partype
                    param_lst = [self.visit(i, c)[1] for i in ast.param]
                    if len(partype_lst) != len(param_lst):
                        raise TypeMismatchInStatement(ast)
                    for i in range(len(param_lst)):
                        self.check_type(partype_lst[i], param_lst[i], ast, flag=0)
                    return
        else:
            val, typ, isVar = self.visit(ast.obj, c)
        if type(typ) is not ClassType:
            raise TypeMismatchInStatement(ast)
        local_envi = self.glob[typ.classname.name]
        func_val = func_typ = None
        flag = False
        for i in local_envi:
            if i.name == ast.method.name and type(i.mtype) is MType:
                if not i.isInst:
                    raise IllegalMemberAccess(ast)
                func_val, func_typ = i.value, i.mtype
                flag = True
                break
        if not flag:
            raise Undeclared(Method(), ast.method.name)

        if type(func_typ) is not MType:
            raise TypeMismatchInStatement(ast)
        if type(func_typ.rettype) is not VoidType:
            raise TypeMismatchInStatement(ast)
        partype_lst = func_typ.partype
        param_lst = [self.visit(i, c)[1] for i in ast.param]

        if len(partype_lst) != len(param_lst):
            raise TypeMismatchInStatement(ast)
        for i in range(len(param_lst)):
            self.check_type(partype_lst[i], param_lst[i], ast)

    def visitArrayCell(self, ast, c):
        """
        class ArrayCell(LHS):
            arr: Expr
            idx: List[Expr]
        """
        ret_val, ret_typ, isVar = self.visit(ast.arr, c)
        if type(ret_typ) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        idx_count = len(ast.idx) # a[1][2][3]
        while type(ret_typ) is ArrayType and idx_count > 0:
            ret_typ = ret_typ.eleType
            idx_count -= 1
        if idx_count > 0:
            raise TypeMismatchInExpression(ast)
        for i in ast.idx:
            val, typ, _ = self.visit(i, c)
            if type(typ) is not IntType:
                raise TypeMismatchInExpression(ast)

        return None, ret_typ, isVar


    def visitBinaryOp(self, ast, c):
        """
        class BinaryOp(Expr):
            op: str
            left: Expr
            right: Expr
        """
        op = ast.op
        left_val, left_type, isVar_left = self.visit(ast.left, c)
        right_val, right_type, isVar_right = self.visit(ast.right, c)

        if isVar_left == 1 or isVar_right == 1:
            isVar = 1
        else:
            isVar = 0
        if op in ['+', '-',  '*',  '/',  '<', '<=', '>', '>=']:
            if (type(left_type) is FloatType and type(right_type) is IntType) or (type(right_type) is FloatType and type(left_type) is IntType) or (type(right_type) is FloatType and type(left_type) is FloatType):
                return None, FloatType() if op in ['+','-','*','/'] else BoolType(), isVar
            elif type(left_type) is IntType and type(right_type) is IntType:
                return None, IntType() if op in ['+','-','*','/'] else BoolType(), isVar
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['==', '!=']:
            if type(left_type) is IntType and type(right_type) is IntType:
                return None, BoolType(), isVar
            elif type(left_type) is BoolType and type(right_type) is BoolType:
                return None, BoolType(), isVar
            else:
                raise TypeMismatchInExpression(ast)
        elif op == '%':
            if type(left_type) is IntType and type(right_type) is IntType:
                return None, IntType(), isVar
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['&&', '||']:
            if type(left_type) is BoolType and type(right_type) is BoolType:
                return None, BoolType(), isVar
            else:
                raise TypeMismatchInExpression(ast)
        elif op == '==.':
            if type(left_type) is StringType and type(right_type) is StringType:
                return None, BoolType(), isVar
            else:
                raise TypeMismatchInExpression(ast)
        elif op == '+.':
            if type(left_type) is StringType and type(right_type) is StringType:
                return None, StringType(), isVar
            else:
                raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        """
        class UnaryOp(Expr):
            op: str
            body: Expr
        """
        op = ast.op
        body_val, body_typ, isVar = self.visit(ast.body, c)
        if op == '-':
            if type(body_typ) is FloatType:
                return None, FloatType(), isVar
            elif type(body_typ) is IntType:
                return None, IntType(), isVar
            else:
                raise TypeMismatchInExpression(ast)
        elif op == '!':
            if type(body_typ) is BoolType:
                return None, BoolType(), isVar
            else:
                raise TypeMismatchInExpression(ast)





    def visitIntLiteral(self,ast, c): 
        return ast.value, IntType(), 0

    def visitFloatLiteral(self,ast, c):
        return ast.value, FloatType(), 0
    
    def visitStringLiteral(self,ast, c):
        return ast.value, StringType(), 0

    def visitBooleanLiteral(self,ast, c):
        return ast.value, BoolType(), 0

    def visitArrayLiteral(self, ast, c):
        """
        class ArrayLiteral(Literal):
            value: List[Expr]
        """
        val_lst = [self.visit(i, c)[0] for i in ast.value]
        typ_lst = [self.visit(i, c)[1] for i in ast.value]
        isVar_lst = [self.visit(i, c)[2] for i in ast.value]
        for i in typ_lst:
            if type(i) is not type(typ_lst[0]):
                raise IllegalArrayLiteral(ast)
            elif type(i) is ArrayType and type(typ_lst[0]) is ArrayType:
                if i.size != typ_lst[0].size:
                    raise IllegalArrayLiteral(ast)
        return val_lst, ArrayType(len(val_lst), typ_lst[0]), 0

    def visitNullLiteral(self, ast, c):
        return None, None, 0

    def visitSelfLiteral(self, ast, c):
        return None, ClassType(Id(self.current_class)), 0