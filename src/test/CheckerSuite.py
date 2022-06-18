import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: int main() {} """
        input = """
                    Class Program1{}
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_2(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        main1(){}
                        main2(){}
                        main(){
                            Return 1;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_3(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        main(a:Int){
                        }
                    }
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_4(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        main(){
                        }
                    }
                    Class Program{}
                """
        expect = "Redeclared Class: Program"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_5(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        main(){
                        }
                        main(){}
                    }

                """
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_6(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        main1(a:Int; a:Float){
                        }
                        main(){}
                    }

                """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_7(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        main1(a:Int){
                            Val a: Int;
                        }
                        main(){}
                    }

                """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_8(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        main(){}
                        Var a: Int = 2;
                        Val a: Float = 3.5;
                    }

                """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_9(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        main(){
                        }
                        Constructor(){
                        }
                    }
                    Class Program1{
                        main(){
                        }
                        Constructor(){
                            Return 2;
                        }
                    }

                """
        expect = "Type Mismatch In Statement: Return(IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_10(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        Var a:Int = b;
                        main(){
                        }
                        Constructor(){}
                    }

                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_11(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        Var a:Int = 5;
                        main(){}
                        main1(x:Int; y:Float){
                            Var a:Float;
                            Var b:Int = a;
                            Var c:Int = 1;
                            Return a;
                        }
                        Constructor(){}
                    }

                """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),IntType,Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_12(self):
        """Simple program: int main() {} """
        input = """
                    Class Program2{
                        Var c: Int = 5;
                        Var b: Int = 5;
                    }

                    Class Program3{
                        Var cac: Int = 5;
                        main1(){
                            Var a: Int = cac;
                        }
                    }

                    Class Program{
                        main(){}
                        Var b: Int = 5;
                        Var a: Int = 66;
                    }
                """
        expect = "Undeclared Identifier: cac"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_13(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cac: Int = 1000;
                    }
                    Class Program:haha{
                        main1(){
                            Val cac: Float = 3;
                            Return cac;
                        }
                        main(){}
                        Var a: Int = 5;
                        Val b: Int = 6;
                        Val cac: Int = 123;
                        Val b:Int= 3;
                    }
                """
        expect = "Redeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_14(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cac: Int = 1000;
                    }
                    Class Program:haha{
                        main1(){
                            Val cac: haha = New haha();
                            Return cac;
                        }
                        main(){}
                        Var a: Int = 5;
                        Val b: Int = 6;
                        Val cac: Int = 123;
                        Val b: Int = 6;
                    }
                """
        expect = "Redeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_15(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int = 1000;
                    }
                    Class Program:haha{
                        main1(){
                            Val c: haha = New haha();
                            Var l: Float = c.cc;
                            Return c;
                        }
                        main(){}
                        Var a: Int = 5;
                        Val b: Int = 6;
                        Val cac: Int = 123;
                        Val b: Int = 3;
                    }
                """
        expect = "Redeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_16(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int = 1000;
                        func(){
                            Return 1;
                        }
                    }
                    Class hoho{
                        Val ll: haha = New haha();
                    }
                    Class Program:haha{
                        main1(){
                            Val c: haha = New haha();
                            Var t: hoho = New hoho();
                            Var l: Float = c.func();
                            Var m: haha = t.ll;
                            Var h: String = t.func();
                            Return c;
                        }
                        main(){}
                        Var a: Int = 5;
                        Val b: Int = 6;
                        Val cac: Int = 123;
                    }
                """
        expect = "Undeclared Method: func"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_17(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int = 1000;
                        func(){
                            Return 1;
                        }
                    }
                    Class hoho{
                        Val ll: haha = New haha();
                    }
                    Class Program:haha{
                        main1(){
                            Val c: haha = New haha();
                            Var t: hoho = New hoho();
                            Var l: Float = c.func();
                            Var m: haha = t.ll;
                            Var h: String = t.func();
                            Return c;
                        }
                        main(){}
                        Var a: Int = 5;
                        Val b: Int = 6;
                        Val cac: Int = 123;
                    }
                """
        expect = "Undeclared Method: func"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_18(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class hoho{
                        Val ll: haha = New haha();
                    }
                    Class Program:haha{
                        main1(){
                            Val c: Int = 2;
                            c = 3;
                        }
                        main(){}
                        Var a: Int = 5;
                        Val b: Int = 6;
                        Val cac: Int = 123;
                    }
                """
        expect = "Cannot Assign To Constant: AssignStmt(Id(c),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_19(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class hoho{
                        Val ll: haha = New haha();
                    }
                    Class Program:haha{
                        Var a: Int = 5;
                        Val b: Int = 6;
                        Val cac: Int = 123;
                        main1(){
                            b = 5;
                        }
                        main(){}

                    }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_20(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Val a: Int = 1;
                        main(){
                           a = cc;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_21(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Int = cc;
                        main(){
                           Val b: Int = 1;
                           a = cc;
                           Foreach (b In 1 .. 100 By 2){
                                a = 5;
                           }
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_22(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Int = cc;
                        main(){
                           Var b: Int;
                           a = cc;
                           Foreach (b In 1.2 .. 100 By 2){
                                a = 5;
                           }
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_23(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Int = cc;
                        main(){
                           Var b: Int;
                           a = cc;
                           If(1){
                           }
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_24(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Float;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Int;
                        main(){
                           Var b: Int;
                           a = cc;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_25(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Float;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Int;
                        main(){
                           Var b: Int;
                           a = b;
                           b = cc;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_26(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Float;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Int;
                        main(){
                           Var b: Int;
                           a = b;
                           b = cc;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_27(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Float;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Int = cc;
                        main(){
                           Var b: Int;
                           a = b;
                           b = cc;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,Id(cc))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_28(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Int = cc;
                        main(){
                           Var b: Float = cc;
                           b = a;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_29(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Int = cc;
                        main(){
                           Var b: Float = cc;
                           b = a;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_30(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Array[Int, 2] = Array(1.5,2);
                        main(){
                        }
                    }
                """
        expect = "Illegal Array Literal: [FloatLit(1.5),IntLit(2)]"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_31(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Array[Int, 2] = Array(1,2,3);
                        main(){
                        }
                    }
                """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),ArrayType(2,IntType),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_32(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Array[Int, 2];
                        main(){
                            a = Array(1,2,3);
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_33(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Array[Float, 2];
                        main(){
                            a = Array(1,2);
                            a = Array(1.2,2.2);
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_34(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Array[Float, 2];
                        main(){
                            Var a: Array[Float, 3] = Array(1,2,3,5);
                        }
                    }
                """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),ArrayType(3,FloatType),[IntLit(1),IntLit(2),IntLit(3),IntLit(5)])"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_35(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 2.5;
                            Return 1;
                        }
                    }
                    Class Program:haha{
                        Var a: Array[Float, 2];
                        main(){
                            Var a: Array[Float, 3] = Array(1,2,3,5);
                        }
                    }
                """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_36(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 2.5;
                        }
                        func2(a:Int){}
                    }
                    Class Program:haha{
                        Var a: Array[Float, 2];
                        Val b: haha;
                        main(){
                            Var a: Array[Float, 3] = Array(1,2,3);
                            b.func2(1.3);
                        }
                    }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_37(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 2.5;
                        }
                        func2(a:Float){}
                    }
                    Class Program:haha{
                        Var a: Array[Float, 2];
                        Val b: haha;
                        main(){
                            Var a: Array[Float, 3] = Array(1,2,3);
                            b.func2(1,2);
                        }
                    }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_38(self):
        """Simple program: int main() {} """
        input = """
                    Class hoho{
                        Var cl: Float;
                    }
                    Class haha{
                        Var cc: hoho;
                        func(){
                            Return 2.5;
                        }
                        func2(a:Float){}
                    }
                    Class Program:haha{
                        Var a: Array[Float, 2];
                        Val b: haha;
                        main(){
                            Var a: Int = b.cc.cl;
                            b.func2(1,2);
                        }
                    }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_39(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int;
                        func(){
                            Return 2.5;
                        }
                        func2(a:Float){}
                    }
                    Class Program:haha{
                        Var a: Array[Float, 2];
                        Val b: haha;
                        main(){
                            b[0][1] = 2;
                        }
                    }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_40(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        Var a: Array[Float, 2];
                        main(){
                            a[0][1.2] = 2;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_42(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        Var a: Array[Float, 2];
                        main(){
                            a[0] = (1+2)*3.5/3;
                            a[1] = "str" + 4;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_43(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        Var a: Array[String, 2];
                        main(){
                            a[1] = ("str" +. "func") ==. "go";
                            a[1] = True && False + 3;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_44(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        Var a: Array[String, 2];
                        main(){
                            a[1] = ("str" +. "func") ==. "go";
                            a[1] = True && False + 3;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_45(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        Var a: Array[String, 2];
                        main(){
                            a[1] = ("str" +. "func") ==. "go";
                            a[1] = True && False + 3;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_46(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int = 3;
                        func(){
                            Return 2;
                        }
                    }
                    Class Program{
                        Var a: Array[String, 2];
                        main(){
                            Var a: haha = New haha();
                            Var c: Int = 0;
                            Var in: String;
                            c = a.func() * 2 - a.cc/3;
                            in = a.func();
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(in),CallExpr(Id(a),Id(func),[]))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_47(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int = 3;
                        func(){
                            Return 2;
                        }
                    }
                    Class Program{
                        Val a: Array[String, 2] = 3;
                        main(){
                            Var a: haha = New haha();
                            Var c: Int = 0;
                            Var in: String;
                            c = a.func() * 2 - a.cc/3;
                            in = a.func();
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),ArrayType(2,StringType),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_48(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var cc: Int = 3;
                        func(){
                            Return 2;
                        }
                    }
                    Class Program{
                        Var a: Array[String, 2];
                        main(){
                            Val a: haha = 3;
                            Var c: Int = 0;
                            Var in: String;
                            c = a.func() * 2 - a.cc/3;
                            in = a.func();
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),ClassType(Id(haha)),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_49(self):
        """Simple program: int main() {} """
        input = """
                    Class hoho{
                        Var dd: Int = 2;
                    }
                    Class haha{
                        Var cc: Int = 3;
                        Var $cc: hoho = New hoho();
                        func(){
                            Return 2;
                        }
                    }
                    Class Program{
                        Var a: Array[String, 2];
                        main(){
                            Var a: haha = New haha();
                            Var f: Int = haha::$cc.dd;
                            Var t: Int = a::$cc.dd;
                        }
                    }
                """
        expect = "Illegal Member Access: FieldAccess(Id(a),Id($cc))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_50(self):
        """Simple program: int main() {} """
        input = """
                    Class hoho{
                        Var dd: Int = 2;
                    }
                    Class haha{
                        Var cc: Int = 3;
                        Var $cc: hoho = New hoho();
                        func(){
                            Return 2;
                        }
                        $func(){
                            Return 3;
                        }
                    }
                    Class Program{
                        Var a: Array[String, 2];
                        main(){
                            Var a: haha = New haha();
                            Var f: Int = haha::$cc.dd;
                            Var t: Int = haha::$func();
                            Var g: Int = a::$func();
                        }
                    }
                """
        expect = "Illegal Member Access: CallExpr(Id(a),Id($func),[])"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_51(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        Var a: Array[String, 2];
                        main(){
                            Val a:Int;
                        }
                    }
                """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_52(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                        Var a: Array[String, 2];
                        main(){
                            Var b:Int = 2;
                            Val a:Int = 1 + 2/3 -5*6 - b;
                        }
                    }
                """
        expect = "Illegal Constant Expression: BinaryOp(-,BinaryOp(-,BinaryOp(+,IntLit(1),BinaryOp(/,IntLit(2),IntLit(3))),BinaryOp(*,IntLit(5),IntLit(6))),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_53(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var b:Int;
                        Val c:Int = 3;
                    }
                    Class Program{
                        Var a: Array[String, 2];
                        main(){
                            Var d:haha = New haha();
                            Var b:Int = 2;
                            Val a:Int = 1 + 2/3 -5*6 - d.c;
                            Val aa:Int = 1 - 2/d.b;
                        }
                    }
                """
        expect = "Illegal Constant Expression: BinaryOp(-,IntLit(1),BinaryOp(/,IntLit(2),FieldAccess(Id(d),Id(b))))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_54(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var b:Int;
                        Val c:Int = 3;
                    }
                    Class Program{
                        Var d:haha = New haha();
                        Var b:Int = 2;
                        Val a:Int = 1 + 2/3 -5*6 - d.c;
                        Val aa:Int = 1 - 2/d.b;
                        main(){

                        }
                    }
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_55(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var b:Int;
                        Val c:Int = 3;
                    }
                    Class Program{
                        Var d:haha = New haha();
                        Var b:Int = 2;
                        Val a:Int = 1 + 2/3 -5*6 - d.c;
                        Val aa:Int = 1 - 2/d.b;
                        main(){

                        }
                    }
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_56(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var a:Int = 3;
                    }
                    Class Program{
                        Var d,e,b:Int = 1,2,3;
                        main(){
                            d = Self.d + Self.e + Self.b;
                            e = Self.a;
                        }
                    }
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_57(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var a:Int = 3;
                        Constructor(a,b:Int; c:Float){}
                    }
                    Class Program{
                        Var d,e,b:Int = 1,2,3;
                        main(){
                            d = Self.d + Self.e + Self.b;
                            Var l:haha = New haha(1,2,1.1);
                            Var lol:haha = New haha();
                        }
                    }
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_58(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var a:Int = 3;
                        Constructor(a,b:Int; c:Float){}
                    }
                    Class Program{
                        Var d,e,b:Int = 1,2,3;
                        main(){
                            d = Self.d + Self.e + Self.b;
                            Var l:haha = New haha(1,2,1.1);
                            Var lol:haha = New haha(1);
                        }
                    }
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_59(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var a:Int = 3;
                        Constructor(a,b:Int; c:Float){}
                    }
                    Class Program{
                        Var d,e,b:Int = 1,2,3;
                        main(){
                            d = Self.d + Self.e + Self.b;
                            Var l:haha = New haha(1,2,1.1);
                            Var lol:haha = New haha(1);
                        }
                    }
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_60(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var a:Int = 3;
                        Constructor(a,b:Int; c:Float){}
                    }
                    Class Program{
                        Var d,e,b:Int = 1,2,3;
                        main(){
                            d = Self.d + Self.e + Self.b;
                            Var l:haha = New haha(1,2,1.1);
                            Var lol:haha = New haha(1, 2, 3);
                            Foreach (d In 1 .. 100 By 2) {
                                If(1*2==3){
                                    Continue;
                                }
                            }
                            Break;
                        }
                    }
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_61(self):
        """Simple program: int main() {} """
        input = """
                    Class haha{
                        Var a:Int = 3;
                        Constructor(a,b:Int; c:Float){}
                    }
                    Class Program{
                        Var d,e,b:Int = 1,2,3;
                        main(){
                            d = Self.d + Self.e + Self.b;
                            Var l:haha = New haha(1,2,1.1);
                            Var lol:haha = New haha(1, 2, 3);
                            Foreach (d In 1 .. 100 By 2) {
                                If(1*2==3){
                                    Continue;
                                    Foreach(e In 2 .. 3 By 100){
                                        Continue;
                                    }
                                    Break;
                                }
                            }
                        }
                    }
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_62(self):
        """Simple program: int main() {} """
        input = """
                    Class A {

                        goo(){Return 1;}

                        foo(){

                            Var x : Int = Self.goo; 

                        }

                    }
                """
        expect = "Undeclared Attribute: goo"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_63(self):
        """Simple program: int main() {} """
        input = """
                    Class A {

                        Var goo : Int = 1;

                        foo(){

                            Var x : Int = Self.goo(); 

                        }

                    }
                """
        expect = "Undeclared Method: goo"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_64(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{

                        Val $someStatic : Int = 10;

                        main() {

                            Var Program : Float = 1.0;

                            Var x : Int = Program::$someStatic; 
                            Var x : Int;
                       }

                    }
                """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_65(self):
        """Simple program: int main() {} """
        input = """
                    Class A {
                      Var foo: Int = 1;
                      foo() {
                        ## Body code ##
                      }
                    }

                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_66(self):
        """Simple program: int main() {} """
        input = """
                    Class A {
                      foo() {
                        ## Body code ##
                        Var foo: Int = 1;
                      }  
                      Var foo: Int = 1; 
                    }

                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_67(self):
        """Simple program: int main() {} """
        input = Program(
            [
                ClassDecl(
                    Id('Program'),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([
                                ConstDecl(
                                    Id("myVar"),
                                    IntType(),
                                    IntLiteral(5)
                                ),
                                Assign(
                                    Id("myVar"),
                                    IntLiteral(10)
                                )]
                            )
                        )
                    ]
                )
            ]
        )
        expect = "Cannot Assign To Constant: AssignStmt(Id(myVar),IntLit(10))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):
        input = """Class Program{ main(a:Int){} Var x: Boolean = ((3 / 4) < 5) || !True || False; }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        input = """Class Program{ main(a:Int){} Var x: Boolean = ("hello" +. "world") ==. "helloworld"; }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        input = """Class Program{ main(){} Var x: Boolean = (1.0 == 2.0) && False; }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLit(1.0),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        input = """Class Program{ main(a:Int){} Var x: Boolean = (True == False) || (1 != 2) && False; }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        input = """Class Program{ main(){} Var x: String = 1 == 2; }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(x),StringType,BinaryOp(==,IntLit(1),IntLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = """
        Class A{
            Var a, d: Int;
            sickle(s: String; e: Int){
                Foreach(i In Self.a .. 10 By Self.d){
                   Break;
                   Continue;
                }
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        input = """
        Class A {
            Var a: Array[Int, 1] = Array(1, 2, 3, 4);
            Var b: Array[Int, 1] = Array(True);
            Var d,e: Int;
            Val f: Array[Array[Int,1], 2] = Array( Array(d), Array(e) );
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),ArrayType(1,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        input = """
        Class A {
            Var b: Array[Int, 1] = Array(True);
            Var d,e: Int;
            Val f: Array[Array[Int,1], 2] = Array( Array(d), Array(e));
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),ArrayType(1,IntType),[BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        input = """
        Class A {
            Var b: Array[Int, 1] = Array(True);
            Var d,e: Int;
            Val f: Array[Array[Int,1], 2] = Array( Array(d), Array(e));
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),ArrayType(1,IntType),[BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        input = """
        Class A {
            Val a: Array[Int, 4] = Array(1,2,3,4);
            foo() {
                Val a : Array[Int, 3] = Array(Self.a, 1, 2);
                Val b : Int = a[0];
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Illegal Array Literal: [FieldAccess(Self(),Id(a)),IntLit(1),IntLit(2)]"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        input = """
        Class Program{
            Val $someStatic : Int = 10;
            main() {
                Var Program : Float = 1.0;
                Var x : Int = Program::$someStatic;
                Var d: Int = 1 && 3.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,IntLit(1),FloatLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 477))


    def test_478(self):
        input = """
                Class A {
                    Constructor(){
                        Return 1;
                    }
                }
            """

        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        input = """
                Class A {
                    Constructor(){
                        Return;
                    }
                }
                Class B{
                    foo(){
                        Var b:A = New A();
                    }
                }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
        input = """
                Class Program {
                    Var a: Int;
                    Val b: Int = 0;
                    Var c: Int;
                    Val arr: Array[Int,2] = Array(1, Self.a);
                    Val test3: Int = Self.arr[Self.b];
                    Val test3: Int = Self.arr[Self.c];
                }
            """

        expect = "Redeclared Attribute: test3"
        self.assertTrue(TestChecker.test(input, expect, 480))


    def test_481(self):
        input = """
                Class Program{
                      foo(){
                        Val x: Int = 1;
                        Return x;
                      }
                      foo2(){
                       Var x: Int = 1;
                       Return x;
                      }
                      foo3(){
                        Val y1: Int = Self.foo() + 1; ## OK since Self.foo() return Constant ##
                        Val y2: Int = Self.foo2() + 1; ## Raise error because Self.foo2() return Variable ##
                      }
                      main(){}
                }
            """

        expect = "Illegal Constant Expression: BinaryOp(+,CallExpr(Self(),Id(foo2),[]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 481))


    def test_482(self):
        input = """
                Class Program{
                    foo(){}
                    $someStaticMethod(){
                        Self.foo();
                    }
                }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 482))


    def test_483(self):
        # NOTE: This case check for param compatiblity of Constructor
        input = """
                        Class A
                        {
                        }
                        Class B:A
                        {
                            Var a: A = New B();
                        }
            """

        expect = "Type Mismatch In Statement: VarDecl(Id(a),ClassType(Id(A)),NewExpr(Id(B),[]))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        input = """
                        Class Program{
                            Val $someStatic : Int = 10;
                            foo() {
                                Var Program : Float = 1.0;
                                Var x : Int = Program::$someStatic;
                           }
                        }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        """Simple program: int main() {} """
        input = """
                        Class A {
                           $fooExp1(x:Float; y:String){
                                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                Var b: Array[Array[Int, 2],2] = Array(Array("a","a"),Array("a","abc"));
                           }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(b),ArrayType(2,ArrayType(2,IntType)),[[StringLit(a),StringLit(a)],[StringLit(a),StringLit(abc)]])"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        """Simple program: int main() {} """
        input = """
                        Class A {
                           $fooExp1(x:Float; y:String){
                                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1,"a"));
                           }
                        }"""
        expect = "Illegal Array Literal: [IntLit(1),IntLit(1),StringLit(a)]"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        """Simple program: int main() {} """
        input = """
                        Class A {
                           $fooExp1(){
                                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                a[1] = Array(1,1);
                                a[1][1] = 1;
                                a = 1;
                           }
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 487))


    def test_488(self):
        input = """
                        Class Program{
                            Val $someStatic : Int = 10;
                            foo() {
                                Var Program : Float = 1.0;
                                Var x : Int = Program::$someStatic;
                           }
                        }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = """
        Class Program {
            mainN() {
                Var a: Boolean = !True;
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        input = """
        Class Program {
            mainN() {
                Var a: Boolean = !True;
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """
            Class B {
                Var $a: Int = 1;
                Val $b: Int = 2;
                foo(){
                    Val c: Int = 1;
                    Return 1;
                }
            }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"), [
                        MethodDecl(Static(), Id("main"), [], Block([])),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("myVar"), StringType(),
                                StringLiteral("Hello World")
                            )
                        ),
                        AttributeDecl(
                            Instance(), VarDecl(Id("myVar"), IntType())
                        )
                    ]
                )
            ]
        )
        expect = """Redeclared Attribute: myVar"""
        self.assertTrue(TestChecker.test(input, expect, 492))


    def test_493(self):
        input = """
            Class A {
                Var a: Int = 1;
            }
            Class B{
                Var b:A = New A();
            }
            Class C{
                foo(){
                    Var c:B = New B();
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """
            Class A {
                Var a: Int = 1;
            }
            Class B{
                Var $b:A = New A();
            }
            Class C{
                foo(){
                    Var c:B = New B();
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = """
            Class A {
                Var a: Int = 1;
            }
            Class B{
                Var $b:A = New A();
            }
            Class C{
                foo(){
                    Var c:B = New B();
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 495))


    def test_496(self):
        input = """
                        Class Z{
                            m(){
                                Var y:String = "1";
                                Var x:Int = 1;
                                If (True){
                                    Var y:Int = 2;
                                }
                                Elseif(True){
                                    Var y:Int = 2;
                                }
                                Else{
                                    Var y:Int = 2;
                                }
                                Var x:Int = 2022 ;
                            }
                        }
                        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 496))


    def test_497(self):
        input = """
        Class Z{
            m(){
                Var z:String = "xyz" +. "abc";
                Var d:Boolean = ("xyz" +. "abc") ==. "def";
                Var m:String = ("xyz" ==. "abc") +. "def";
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+.,BinaryOp(==.,StringLit(xyz),StringLit(abc)),StringLit(def))"
        self.assertTrue(TestChecker.test(input, expect, 497))


    def test_498(self):
        input = """
                        Class Z{
                            m(){
                                Var z:Float = --------1.22;
                                Var d:Boolean = !((("abc" +. "def") ==. "ghi") || False);
                                Var m:Float = !!!!--1.22;
                            }
                        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,UnaryOp(-,UnaryOp(-,FloatLit(1.22))))"
        self.assertTrue(TestChecker.test(input, expect, 498))


    def test_499(self):
        input = """
                Class A{
                    Var b,c,d,e,f,g,h,i,k,l,m,n,o,p,q: Int;
                }
                Class B{
                    a(){}
                    b(){}
                    c(){}
                    d(){}
                    e(){}
                    f(){}
                    g(){}
                    g(){}
                }
                """
        expect = "Redeclared Method: g"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_500_FINALTEST(self):
        input = """
                Class Program{
                    main(){}
                    g(){}
                    g(){}
                }
                """
        expect = "Redeclared Method: g"
        self.assertTrue(TestChecker.test(input, expect, 500))