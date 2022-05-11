from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

from functools import reduce


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([self.visit(x) for x in ctx.class_declare()])

    # Visit a parse tree produced by D96Parser#class_declare.
    def visitClass_declare(self, ctx: D96Parser.Class_declareContext):
        # cl_body = [x for i in ctx.class_body() for x in self.visit(i)]
        cl_body = [self.visit(i) for i in ctx.class_body()]
        mem_dec = []
        for mem in cl_body:
            if isinstance(mem, list):
                mem_dec += [i for i in mem]
            else:
                mem_dec += [mem]
        if len(ctx.ID()) == 2:
            return ClassDecl(Id(ctx.ID(0).getText()), mem_dec, Id(ctx.ID(1).getText()))
        else:
            return ClassDecl(Id(ctx.ID(0).getText()), mem_dec)

    # Visit a parse tree produced by D96Parser#att_declare.
    def visitAtt_declare(self, ctx:D96Parser.Att_declareContext):  # not yet for expr case
        mutable = True if ctx.VAR() else False
        mixedList = self.visit(ctx.mixed_list())
        expList = []
        if ctx.exp_list():
            expList = self.visit(ctx.exp_list())
            return [AttributeDecl(siKind, VarDecl(id, self.visit(ctx.type_name()), exp)) for ((id, siKind),exp) in zip(mixedList,expList)] if mutable else [AttributeDecl(siKind, ConstDecl(id, self.visit(ctx.type_name()), exp)) for ((id, siKind),exp) in zip(mixedList,expList)]
        if isinstance(self.visit(ctx.type_name()), ClassType):
            return [AttributeDecl(siKind, VarDecl(id, self.visit(ctx.type_name()), NullLiteral())) for id, siKind in
                    mixedList] if mutable else [AttributeDecl(siKind, ConstDecl(id, self.visit(ctx.type_name()), NullLiteral())) for
                                                id, siKind in mixedList]
        return [AttributeDecl(siKind, VarDecl(id, self.visit(ctx.type_name()))) for id, siKind in mixedList] if mutable else [AttributeDecl(siKind, ConstDecl(id, self.visit(ctx.type_name()))) for id, siKind in mixedList]


    # Visit a parse tree produced by D96Parser#mixed_list.
    def visitMixed_list(self, ctx: D96Parser.Mixed_listContext):
        return [self.visit(i) for i in ctx.member_id()]


    # Visit a parse tree produced by D96Parser#member_id.
    def visitMember_id(self, ctx: D96Parser.Member_idContext):
        return (Id(ctx.ID().getText()), Instance()) if ctx.ID() else (Id(ctx.DOLLARID().getText()), Static())


    # Visit a parse tree produced by D96Parser#method_declare.
    def visitMethod_declare(self, ctx:D96Parser.Method_declareContext):
        if ctx.constructor_declare(): return self.visit(ctx.constructor_declare())
        elif ctx.destructor_declare(): return self.visit(ctx.destructor_declare())
        else:
            id, siKind = self.visit(ctx.member_id())

            parent = ctx.parentCtx
            grand_parent = parent.parentCtx

            if grand_parent.ID(0).getText() == "Program" and id.name == "main" and not ctx.param_list():
                siKind = Static()
            if ctx.param_list():
                paramlst = self.visit(ctx.param_list())
                return MethodDecl(siKind, id, paramlst, self.visit(ctx.body()))
            else: return MethodDecl(siKind, id, [], self.visit(ctx.body()))


    # Visit a parse tree produced by D96Parser#constructor_declare.
    def visitConstructor_declare(self, ctx:D96Parser.Constructor_declareContext):
        if ctx.param_list():
            return MethodDecl(Instance(), Id(ctx.CONSTRUCTOR().getText()), self.visit(ctx.param_list()), self.visit(ctx.cons_des_body()))
        else:
            return MethodDecl(Instance(), Id(ctx.CONSTRUCTOR().getText()), [], self.visit(ctx.cons_des_body()))


    # Visit a parse tree produced by D96Parser#destructor_declare.
    def visitDestructor_declare(self, ctx:D96Parser.Destructor_declareContext):
        return MethodDecl(Instance(), Id(ctx.DESTRUCTOR().getText()), [], self.visit(ctx.cons_des_body()))


    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body.
    def visitBody(self, ctx:D96Parser.BodyContext):
        lst = [self.visit(i) for i in ctx.stmt()]
        statement = []
        for i in lst:
            if isinstance(i, list):
                statement += [x for x in i]
            else:
                statement += [i]
        return Block(statement)

    # Visit a parse tree produced by D96Parser#cons_des_body.
    def visitCons_des_body(self, ctx:D96Parser.Cons_des_bodyContext):
        lst = [self.visit(i) for i in ctx.cons_des_stmt()]
        statement = []
        for i in lst:
            if isinstance(i, list):
                statement += [x for x in i]
            else:
                statement += [i]
        return Block(statement)


    # Visit a parse tree produced by D96Parser#param_list.
    def visitParam_list(self, ctx:D96Parser.Param_listContext):
        lst = [self.visit(i) for i in ctx.id_list_with_type()]  # List((List[Id], Typename))
        return [VarDecl(id, typename) for id_lst, typename in lst for id in id_lst]

    # Visit a parse tree produced by D96Parser#id_list_with_type.
    def visitId_list_with_type(self, ctx:D96Parser.Id_list_with_typeContext):
        return self.visit(ctx.ids_list()), self.visit(ctx.type_name())    # (List[Id], Typename)


    # Visit a parse tree produced by D96Parser#ids_list.
    def visitIds_list(self, ctx:D96Parser.Ids_listContext):
        return [Id(i.getText()) for i in ctx.ID()]                #  List[Id]


    # Visit a parse tree produced by D96Parser#type_name.
    def visitType_name(self, ctx:D96Parser.Type_nameContext):
        return ClassType(Id(ctx.ID().getText())) if ctx.ID() else self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        if ctx.INT(): return IntType()
        elif ctx.FLOAT(): return FloatType()
        elif ctx.STRING(): return StringType()
        else: return BoolType()


    # Visit a parse tree produced by D96Parser#arr_type.
    def visitArr_type(self, ctx:D96Parser.Arr_typeContext):
        int_str = ctx.INTEGER_LITERAL().getText()
        if int_str[0:2] == "0x" or int_str[0:2] == "0X":
            int_lit = int(int_str, 16)
        elif int_str[0:2] == "0b" or int_str[0:2] == "0B":
            int_lit = int(int_str, 2)
        elif int_str[0] != "0":
            int_lit = int(int_str, 10)
        else:
            int_lit = int(int_str[0] + "o" + int_str[1:], 8)
        return ArrayType(int_lit, self.visit(ctx.type_name()))


    # Visit a parse tree produced by D96Parser#cons_des_stmt.
    def visitCons_des_stmt(self, ctx:D96Parser.Cons_des_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_declare.
    def visitVar_declare(self, ctx:D96Parser.Var_declareContext):
        mutable = True if ctx.VAR() else False
        id_lst = [Id(i.getText()) for i in ctx.ID()]
        expList = []
        if ctx.exp_list():
            expList = self.visit(ctx.exp_list())
            return [VarDecl(i, self.visit(ctx.type_name()), exp) for i,exp in list(zip(id_lst, expList))] if mutable else [
                ConstDecl(i, self.visit(ctx.type_name()), exp) for i,exp in list(zip(id_lst, expList))]

        else:
            if isinstance(self.visit(ctx.type_name()), ClassType):
                return [VarDecl(i, self.visit(ctx.type_name()), NullLiteral()) for i in id_lst] if mutable else [
                    ConstDecl(i, self.visit(ctx.type_name()), NullLiteral()) for i in id_lst]
            else:
                return [VarDecl(i, self.visit(ctx.type_name())) for i in id_lst] if mutable else [ConstDecl(i, self.visit(ctx.type_name())) for i in id_lst]


    # Visit a parse tree produced by D96Parser#assignment.
    def visitAssignment(self, ctx:D96Parser.AssignmentContext):
        return Assign(self.visit(ctx.assign_lhs()), self.visit(ctx.assign_rhs()))


    # Visit a parse tree produced by D96Parser#assign_lhs.
    def visitAssign_lhs(self, ctx:D96Parser.Assign_lhsContext):
        if ctx.getChildCount() == 1:
            if ctx.exp():
                return self.visit(ctx.exp())
            else:
                return Id(ctx.getText())
        elif ctx.getChildCount() == 3:
            if ctx.DOT():
                return FieldAccess(self.visit(ctx.exp()), Id(ctx.getChild(2).getText()))
            elif ctx.DOUBLECOLON():
                return FieldAccess(Id(ctx.getChild(0).getText()), Id(ctx.getChild(2).getText()))
        else:
            return ArrayCell(self.visit(ctx.operands()), self.visit(ctx.index()))


    # Visit a parse tree produced by D96Parser#assign_rhs.
    def visitAssign_rhs(self, ctx:D96Parser.Assign_rhsContext):
        return self.visitChildren(ctx)



    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        elifLst = [self.visit(i) for i in ctx.elseif_stmt()]
        ifThen = (self.visit(ctx.exp()), self.visit(ctx.block_stmt()))
        elifLst.insert(0, ifThen)
        if ctx.else_stmt():
            elseStmt = self.visit(ctx.else_stmt())
            elifLst.append(elseStmt)
            return reduce(lambda x, y: If(y[0], y[1], x), elifLst[::-1])
        return reduce(lambda x, y: If(y[0], y[1], x), elifLst[::-1], None)

    # Visit a parse tree produced by D96Parser#elseif_stmt.
    def visitElseif_stmt(self, ctx:D96Parser.Elseif_stmtContext):
        return self.visit(ctx.exp()), self.visit(ctx.block_stmt())


    # Visit a parse tree produced by D96Parser#else_stmt.
    def visitElse_stmt(self, ctx:D96Parser.Else_stmtContext):
        return self.visit(ctx.block_stmt())


    # Visit a parse tree produced by D96Parser#for_stmt.
    def visitFor_stmt(self, ctx:D96Parser.For_stmtContext):
        id = Id("")
        if ctx.ID(): id = Id(ctx.ID().getText())
        elif ctx.DOLLARID(): id = Id(ctx.DOLLARID().getText())
        if ctx.BY():
            return For(id, self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), self.visit(ctx.block_stmt()), self.visit(ctx.exp(2)))
        else:
            return For(id, self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), self.visit(ctx.block_stmt()), IntLiteral(1))


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        else:
            return Return()


    # Visit a parse tree produced by D96Parser#method_invoc_stmt.
    def visitMethod_invoc_stmt(self, ctx:D96Parser.Method_invoc_stmtContext):
        if ctx.instance_method():
            third = self.visit(ctx.instance_method())
            return CallStmt(self.visit(ctx.exp()), third[0], third[1])
        else:
            third = self.visit(ctx.static_method())
            return CallStmt(Id(ctx.getChild(0).getText()), third[0], third[1])


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        lst = [self.visit(i) for i in ctx.stmt()]
        statement = []
        for i in lst:
            if isinstance(i, list):
                statement += [x for x in i]
            else:
                statement += [i]
        return Block(statement)


    # Visit a parse tree produced by D96Parser#relational.
    def visitRelational(self, ctx:D96Parser.RelationalContext):
        return ctx.getText()


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            op = ctx.CONCATSTR().getText() if ctx.CONCATSTR() else ctx.EQSTR().getText()
            return BinaryOp(op, left, right)


    # Visit a parse tree produced by D96Parser#exp1.
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.exp2(0))
            right = self.visit(ctx.exp2(1))
            op = self.visit(ctx.relational())
            return BinaryOp(op, left, right)


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            op = ctx.AND().getText() if ctx.AND() else ctx.OR().getText()
            return BinaryOp(op, left, right)


    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            op = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()
            return BinaryOp(op, left, right)


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.exp4())
            right = self.visit(ctx.exp5())
            op = ctx.MUL().getText() if ctx.MUL() else ctx.DIV().getText() if ctx.DIV() else ctx.MODULO().getText()
            return BinaryOp(op, left, right)


    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            one = self.visit(ctx.exp5())
            op = ctx.NOT().getText()
            return UnaryOp(op, one)


    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            one = self.visit(ctx.exp6())
            op = ctx.SUB().getText()
            return UnaryOp(op, one)


    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            one = self.visit(ctx.exp7())
            return ArrayCell(one, self.visit(ctx.index()))


    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.exp8())
            right = self.visit(ctx.exp9())
            if isinstance(right, tuple):
                return CallExpr(left, right[0], right[1])
            else:
                return FieldAccess(left, right)


    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.exp9())
            right = self.visit(ctx.exp10())
            if isinstance(right, tuple):
                return CallExpr(left, right[0], right[1])
            else:
                return FieldAccess(left, right)


    # Visit a parse tree produced by D96Parser#exp10.
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            one = self.visit(ctx.exp10())
            op = ctx.NEW().getText()
            return NewExpr(one[0], one[1])



    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        if ctx.literal(): return self.visitChildren(ctx)
        elif ctx.ID() or ctx.DOLLARID(): return Id(ctx.getText())
        elif ctx.index(): return self.visit(ctx.index())
        elif ctx.instance_method(): return self.visit(ctx.instance_method())
        elif ctx.static_method(): return self.visit(ctx.static_method())
        elif ctx.obj_create(): return self.visitChildren(ctx)
        elif ctx.LP(): return self.visit(ctx.exp())
        else : return None




    # Visit a parse tree produced by D96Parser#index.
    def visitIndex(self, ctx:D96Parser.IndexContext):
        if ctx.index():
            return [self.visit(ctx.exp())] + self.visit(ctx.index())
        else:
            return [self.visit(ctx.exp())]


    # Visit a parse tree produced by D96Parser#instance_method.
    def visitInstance_method(self, ctx:D96Parser.Instance_methodContext):
        if ctx.exp_list():
            return (Id(ctx.ID().getText()), self.visit(ctx.exp_list()))
        else:
            return (Id(ctx.ID().getText()), [])


    # Visit a parse tree produced by D96Parser#static_method.
    def visitStatic_method(self, ctx:D96Parser.Static_methodContext):
        if ctx.exp_list():
            return (Id(ctx.DOLLARID().getText()), self.visit(ctx.exp_list()))
        else:
            return (Id(ctx.DOLLARID().getText()), [])

    # # Visit a parse tree produced by D96Parser#instance_invoc_exp.
    # def visitInstance_invoc_exp(self, ctx: D96Parser.Instance_invoc_expContext):
    #     if ctx.instance_method():
    #         third = self.visit(ctx.instance_method())
    #         return CallExpr(Id(ctx.getChild(0).getText()), third[0], third[1])
    #     else:
    #         return FieldAccess(Id(ctx.getChild(0).getText()), Id(ctx.getChild(2).getText()))
    #
    # # Visit a parse tree produced by D96Parser#static_invoc_exp.
    # def visitStatic_invoc_exp(self, ctx: D96Parser.Static_invoc_expContext):
    #     if ctx.static_method():
    #         third = self.visit(ctx.static_method())
    #         return CallExpr(Id(ctx.getChild(0).getText()), third[0], third[1])
    #     else:
    #         return FieldAccess(Id(ctx.getChild(0).getText()), Id(ctx.getChild(2).getText()))


    # Visit a parse tree produced by D96Parser#obj_create.
    def visitObj_create(self, ctx:D96Parser.Obj_createContext):
        if ctx.exp_list():
            return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.exp_list()))
        else:
            return NewExpr(Id(ctx.ID().getText()), [])


    # Visit a parse tree produced by D96Parser#exp_list.
    def visitExp_list(self, ctx:D96Parser.Exp_listContext):
        return [self.visit(exp) for exp in ctx.exp()]


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        if ctx.INTEGER_LITERAL():
            int_str = ctx.INTEGER_LITERAL().getText()
            if int_str[0:2] == "0x" or int_str[0:2] == "0X":
                return IntLiteral(int(int_str, 16))
            elif int_str[0:2] == "0b" or int_str[0:2] == "0B":
                return IntLiteral(int(int_str, 2))
            elif int_str[0] != "0":
                return IntLiteral(int(int_str, 10))
            else:
                return IntLiteral(int(int_str[0] + "o" + int_str[1:], 8))
        elif ctx.FLOAT_LITERAL():
            float_str =  ctx.FLOAT_LITERAL().getText()
            if float_str[0] == '.':
                float_str = "0" + float_str
            return FloatLiteral(float(float_str))
        elif ctx.ZERO_INTLIT(): return IntLiteral(int(ctx.ZERO_INTLIT().getText(), 0))
        elif ctx.STRING_LITERAL(): return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.array_literal(): return self.visitChildren(ctx)
        elif ctx.boolean_literal(): return self.visitChildren(ctx)
        elif ctx.SELF(): return SelfLiteral()
        elif ctx.NULL(): return NullLiteral()
        else: return None
    # Visit a parse tree produced by D96Parser#boolean_literal.
    def visitBoolean_literal(self, ctx:D96Parser.Boolean_literalContext):
        return BooleanLiteral(True if ctx.TRUE() else False)


    # Visit a parse tree produced by D96Parser#array_literal.
    def visitArray_literal(self, ctx:D96Parser.Array_literalContext):
        if len(ctx.array_literal()) >= 1:
            return ArrayLiteral([self.visit(i) for i in ctx.array_literal()])
        else:
            if ctx.exp_list():
                return ArrayLiteral(self.visit(ctx.exp_list()))
            else:
                return ArrayLiteral([])
