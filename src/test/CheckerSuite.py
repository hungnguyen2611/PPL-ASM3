import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test0(self):
        input = """
        Class A{
            Val a: Int = 5;
            a(a,b,c:String; d:Float; e:Int){
                Val g:A = New A();
            }
            method(){
                If(True){

                } Elseif(1+1){

                } Else{

                }
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect ="Type Mismatch In Statement: If(BooleanLit(True),Block([]),If(BinaryOp(+,IntLit(1),IntLit(1)),Block([]),Block([])))"
        self.assertTrue(TestChecker.test(input,expect,0))

    def test1(self):
        input = """
        Class A{
            Var expr:Boolean = True;
        }
        Class Program {
            Val expr:Boolean = True;
            Var $expr:Boolean = False;
            method(){
                Val a:Boolean = True;
                Val c:Boolean = True;
                Val obj:A = New A();
                Var d: Float = 2.0;
                If(a){
                    Val obj:A = New A();
                    {
                        Var obj:A= New A();
                        obj.expr = False;
                    }
                } Elseif (obj.expr){
                    d = d+1;

                } Elseif(Self.expr){
                    d = d + 5.6e-2;
                } Elseif(Program::$expr){
                    d = d +5;
                } Else{
                    If (obj.expr){

                    } Else{
                        d = d + 1;
                        d = d * "Hello world";
                    }
                }

            }
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(d),StringLit(Hello world))"
        self.assertTrue(TestChecker.test(input,expect,1))

    def test2(self):
        """Simple program: int main() {} """
        input = """
        Class Program{
            main(){
                Return;
            }
        }

        Class Base{
            Val $a:Int = 1;
        }

        Class A:Base{
            main(){
                Var b:String ="Hello";
                A::$a = 1 + 1 + "Hello" - b;
            }
        }

        """
        expect = "Undeclared Attribute: $a"
        self.assertTrue(TestChecker.test(input,expect,2))

    def test3(self):
        input = """
        Class D{
            method(){
                Return 1;
            }
            $static(){
                Val a: D = New D();
                Return a;
            }
        }
        Class A:D {
            Val $a:Int= 5;
            Var b: Float;
        }

        Class B:A{
            Var $a:Int = 1;
            getName(){
                Return "Hello world";
            }
            $staticMethod(){
                Return "Hello";
            }
            program(a,b,c:Float; e:String; f:Boolean){
                Return;
            }
        }
        Class Program{
            getName(){
                Var a:B = New B();
                Var b:String;
                Var c:Int = 1;
                b = B::$staticMethod();
                Var B:Float;
                B::$a = 1;
                a.program(1,2.0,3, "Hello", True);
                b = a.getName();
            }
            main(){
                Return;
            }
        }

        Class E:F{

        }
        """
        expect = "Undeclared Class: F"
        self.assertTrue(TestChecker.test(input,expect,3))

    def test4(self):
        input = """
        Class A{
            Var $static:Float = 1;
            Val $obj:A = New A();
            Val obj:A = New A();
            Var a: Int = 5;
            Var b: Int = 1 + A::$obj.a;
            Var c: Int = 1 + Self.obj.a;
            method(){
                Val a: Int = 5;
                Var b: Int = 1 + a;
                Var A:A;
                A = New A();
                A.a = 1;
                A::$static = 6;
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        Class B{

        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,4))

    def test5(self):
        input = """
        Class A{
            Val $atr: Int = 1;
            Var $atrr: String = "Hello";
            Val a:Float = 2;
            Var b: Boolean = True;
            $atr(){
                Return 5;
            }
            a(){
                Return 2.0;
            }
            method(){
                Val A:A = New A();
                Var cal: Int = 1;
                Var f:Float = 5.6;
                A::$atrr = "Hello wordl" +. A::$atrr;
                A.b = False;
                cal = A::$atr() + 5;
                f = A.a() + 3.0;
                Return cal;
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,5))

    def test6(self):
        input = """
        Class B{
            Var att:String;
            Constructor(){
                Return;
            }
        }
        Class A:B{
            method(){
                Val a:Array[Int,2] = Array(1,2);
                Var b:Array[Array[Float,2],2] = Array(Array(1.0, 2.0), Array(3.5, 3.6));
                Var c:Array[Array[Float,2],2] = Array(Array(1, 2), Array(3, 3));
                Var obj_b:B = New B();
                Var obj:B;
            }
        }
        Class Program{
            main(){
                Var i :Int;
                Foreach(i In 1 .. 100){
                    Continue;
                    Break;
                }
                Return;
            }
            Constructor(a,b,c:Int; d:String){
                Return "Hello";
                Continue;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(StringLit(Hello))"
        self.assertTrue(TestChecker.test(input,expect,6))

    def test7(self):
        input = """
        Class B{
            Contructor(){
                Return;
            }
        }
        Class A{
            Var $a: Int; 
            Var b: Int;
            getName(){}
            Constructor(a,b,c:Int; d:String; e:Array[Float,2]; obj:B){
                Return;
            }
            method(){
                Val A: A = New A(1,2,3,"Hello", Array(1.0, 2.0), New B());
                A::$a = 1;
            }
        }

        Class Program{
            Var a:Array[Array[Int,2],2];
            Val c:Boolean = True;
            method(a:Array[Array[Int,2],2]; b:A; c:Boolean){
                Return 123;
            }
            main(){
                Val b:Int = 5;
                Var c:Int = 6;
                Val a:A = New A(b,c,6, "Hello World", Array(2,3), New B());
                Var d: Float = Self.method(Self.a, a, Self.c);
                Var obj:A;
                Return;
            }
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,7))

    def test8(self):
        input = """
        Class B{
            Var c:Int = 6;

        }
        Class A:B{
           Var a:Int;
        }

        Class Program{
            main(){
                Var a:A;
                a.a = 1;
                Self.c = 5;
            }
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,8))

    def test7(self):
        input = """
        Class B{
        }
        Class A:B{
            Var a: Float;
            Var b: Int;
            program(){
                Self.a = Self.b;
            }
            method(a:B){

            }
            $method(b:A){

            }
        }
        Class Program{
            method(){
                Var b:B = New B();
                (New A()).method(b);
                A::$method(New A());
                (New A()).method(New A());
            }
            main(){
                Return;
            }
        }

        """
        expect = """Type Mismatch In Statement: Call(NewExpr(Id(A),[]),Id(method),[NewExpr(Id(A),[])])"""
        self.assertTrue(TestChecker.test(input,expect,7))

    def test8(self):
        input ="""
        Class A{
            Var $a: Int;
            Val $b: String ="Hello";
            Val a: String = "Hello";
            Var b: Int = 1;
            Var c: Int = 3;
            Val d: Float = 2.0;
            getName(a,b,c: Int){
                Val obj: A = New A();
                obj.b = obj.c + 1;
                c = c + 1;
                {
                    Var x: Int;
                    obj.d = obj.d + 1;
                }
            }
        }

        Class B:A{
            Val $c: Float;
            getName(a,b,c: Int){
                c = c + 1;
                Val obj:B = New B();
                obj.b = obj.c + 1;
                obj.d = c + 1; 
            }
        }

        Class D: B{
            Val $d:Float = 12.6;
            Val e: String ="Hello";
            Val obj3: Int = 12;
            getName(a,b,c: Int){
                c = c + 1;
                Val obj:D = New D();
                obj.b = obj.c + 1;
                obj.d = c + 1; 

                Val obj2:A = New D();
                obj2.b = obj2.c + 1;

                Val obj1:B = New D();
                obj2.b = obj2.c + 1;
                D::$a = 1 + 1 * 2;
            }
        }
        Class E{
            Val e: Int = 5;
        }
        Class Program{
            main(){
                D::$a = 1 + 1 * 2;
                D::$b = "Hello";
                B::$c = 2.0;
                Val D: D = New D();
                D::$a = 1;

                D::$d = "Hello" +. "World";
                Return;
            }
        }
        """
        expect ="Cannot Assign To Constant: AssignStmt(FieldAccess(Id(obj),Id(d)),BinaryOp(+,FieldAccess(Id(obj),Id(d)),IntLit(1)))"
        self.assertTrue(TestChecker.test(input,expect,8))

    def test9(self):
        input ="""
        Class A{
            Val a: Int = 1;
            Var b: String = "Hello";
            method(){
                Val a:String ="Hello";
                Var b:A;

            }
            Var c: String;
        }
        Class B{
            Val a: Int = 5;
        }
        Class Program{
            main(){}
        }
        """
        expect ="""[]"""
        self.assertTrue(TestChecker.test(input,expect,9))

    def test10(self):
        input ="""
        Class C{
            Val c: Int = 56;
        }
        Class A:C{
            Val a: Int = 5;
            Var b: String;
            method(){
                Val a:String ="Hello";
                Var b:A;
                c = c + 1;
                Val d: A = New C();
            }
            Var d: Int;
        }
        Class B:A{
            Val a: Int;
            method(a,b,c:A; d:Int; e:String){
                Val f: A = New B();
            }
        }
        Class Program{
            main(){
                Return ;
            }
        }
        """
        expect ="""Undeclared Identifier: c"""
        self.assertTrue(TestChecker.test(input,expect,10))

    def test11(self):
        input ="""
        Class A:B{

        }
        Class B{

        }
        Class Program{
            main(){

            }
        }
        """
        expect ="Undeclared Class: B"
        self.assertTrue(TestChecker.test(input,expect,11))

    def test12(self):
        input ="""
        Class A{
            Val a:Int =  5;
            Var b:String = "Hello";
            getName(){
                Val obj: A = New A();
                obj.b = obj.a + 1; 
            }
        }
        Class Program{
            main(){}
        }
        """
        expect ="Type Mismatch In Statement: AssignStmt(FieldAccess(Id(obj),Id(b)),BinaryOp(+,FieldAccess(Id(obj),Id(a)),IntLit(1)))"
        self.assertTrue(TestChecker.test(input,expect,12))

    def test13(self):
        input = """
        Class A{
            Contructor(a,b,c:Int){
                Return;
            }
            Destructor(){
                Return "Hello";
            }
        }
        Class Program{
            main(){

            }
        }
        """
        expect = "Type Mismatch In Statement: Return(StringLit(Hello))"
        self.assertTrue(TestChecker.test(input,expect,13))

    def test14(self):
        input = """
         Class A{
            Contructor(a,b,c:Int){
                Return "Hello world";
            }
            Destructor(){
                Return "Hello";
            }
        }
        Class Program{
            main(){

            }
        }
        """
        expect = "Type Mismatch In Statement: Return(StringLit(Hello))"
        self.assertTrue(TestChecker.test(input,expect,14))

    def test15(self):
        input ="""
        Class A{
            Val b: Int = 5;
            getName(a:String; b: Int; d: Boolean ){
                Val e:String ="Hello";
                Var g: Int = 5;
                {
                    Val a: Int = 5;
                    Var e: Boolean;
                }
                {
                    Var a: String;
                    Val b: Boolean = True;
                    {
                        Val c:Int = 5;
                        Var d:Boolean = True;
                        {
                            Val b:Int = Self.b;
                            Var b:String;
                        }
                    }
                }

            }
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,15))

    def test16(self):
        input ="""
        Class A{}
        Class B:A{}
        Class C:D{}
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(input,expect,16))

    def test17(self):
        input ="""
        Class A{

        }
        Class Program{
            Val a:Int = 5;
            main(){
                {
                    Var a:Int = 1;
                    a = a + 1;
                    {
                        Var a:Float;
                        {
                            a = a * 5;
                            Var b:Boolean = 1 > 5;

                        }
                        {
                            a = a * 5.0 + 1 / 2 *5.0;
                            Val b:Int = Self.a + 1 + a;
                        }
                    }
                }
            }
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(a)),IntLit(1)),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,17))

    def test18(self):
        input ="""
        Class A{
            Var a:Int;
            Val e:Int = 5;
            Var b:Int = Self.a + 1;
            Val c:Int = Self.e + b;
        }
        Class Program{
            main(){}
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,18))

    def test19(self):
        input ="""
        Class A{
            Val a:Int = 5;

            getName(a,b:String; c:Int){
                Val e:String ="Hello";
                Val d:A = New X();

            }
        }
        Class Program{
            main(){

            }
        }
        """
        expect = "Undeclared Class: X"
        self.assertTrue(TestChecker.test(input,expect,19))

    def test20(self):
        input ="""
        Class B{
            Val c:String = "Hlo";
            Var $e:String ="Hello";
        }
        Class A:B{
            Val a:Int = 5;
            Var a_ :String = "Hello";
            getName(a,b:String; c:Int){
                Val e:String ="Herllo";
                a = "Hello";
                c = Self.a;
                b = (New B()).c;
                b = (B::$e +. Self.a_) +. (New B()).c;
                Val d:B = New A();

            }
        }
        Class Program{
            main(){

            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(d),ClassType(Id(B)),NewExpr(Id(A),[]))"
        self.assertTrue(TestChecker.test(input,expect,20))

    def test21(self):
        input ="""
        Class A{
            Val a:Int = 5;
            Val b:Float = 6;
            Val c:String = "Hello";
            Val e:Float = Self.c + Self.a + Self.b;
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,21))

    def test22(self):
        input ="""
        Class C{
            Var a:Int= 5;
            Val d: Int = 5;
            Val c:Int = 5;
        }
        Class B{
            Var a: C = New C();
            Val $b:Int = 5;
            Val d:C = New C();
        }
        Class A{
            Val a:Int = 5;
            Val d:B = New B();

            getName(a,b:String; c:Int){
                Val f:Int = Self.a + B::$b;
                Val g:Int = Self.a + B::$b + (New C()).c;
                c = Self.d.d.d + c;
            }
        }
        Class Program{
            main(){

            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,22))

    def test23(self):
        input ="""
        Class A{
            Val a:Int = 5;
            getMethod(b:Array[Int,2 ]; a: A){
                Return 1;
            }
            getMethod_(){
                Return 2.0;
            }
            getName(){
                Val a: A = New A();
                Var f:Float = Self.getMethod(Array(1,2), a) + Self.getMethod_();

                Var arr: Array[Int,5];
                Var b:Int = arr[1];

                Var arr_:Array[String, 5];
                Var c_: Int = arr_[1];

                Val d:X = New A();

            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c_),IntType,ArrayCell(Id(arr_),[IntLit(1)]))"
        self.assertTrue(TestChecker.test(input,expect,23))

    def test24(self):
        input ="""
        Class A{
            Var a:Int;

            getName(a,b:Int; c:Int){
                Var f:Int;
                Foreach(f In b .. c){
                    Val a:Boolean = True;
                    If(1 >= 5){
                        Self.a = 7;
                    } Elseif(a){
                        a.b = 5;
                    }
                }

            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,24))

    def test25(self):
        input ="""
        Class A{
            Val a:Int = 5;

            getName(a,b:String; c:Int){
                Val hello: Array[Array[String,2],3] = Array(Array("a", "b"), Array("c", "d"));
            }
        }
        Class Program{
            main(){

            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(hello),ArrayType(3,ArrayType(2,StringType)),[[StringLit(a),StringLit(b)],[StringLit(c),StringLit(d)]])"
        self.assertTrue(TestChecker.test(input,expect,25))

    def test26(self):
        input ="""
        Class A{
            Var a:Int = 5;
            a(){
                Return 1;
            }
            getName(a,b:String; c:Int){
                A.a = 5 + 1;
            }
            Var a:String;
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(A),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,26))

    def test27(self):
        input ="""
        Class B{
            Var $c:Int = 5;
            Val d:Int = 5;
            $c(){
                Return 1;
            }
            d(){
                Return 5;
            }
        }
        Class A{
            Val a:Int = 5;

            getName(a,b:String; c:Int){
                c = B::$c + B::$c();
                c = B.d + B::$d();
                c = (New B()).d + 5 + (New B()).d();
                c = B::$c() + 1;

            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(B),Id(d))"
        self.assertTrue(TestChecker.test(input,expect,27))

    def test28(self):
        input ="""
        Class A{
            Var $a:Int = 5;

            getName(a,b:String; c:Int){
                Val obj:A= New A();
                obj::$a = 5;
            }
        }
        Class Program{
            main(){}
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(obj),Id($a))"
        self.assertTrue(TestChecker.test(input,expect,28))

    def test29(self):
        input ="""
        Class A{
            Var a:Int;

            getName(a,b:String; c:Int){
                Var obj: Int = 5;
                obj.a = 5;
            }
        }
        """
        expect = "Type Mismatch In Expression: FieldAccess(Id(obj),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,29))

    def test30(self):
        input ="""
        Class A{
            Var a:Int;

            getName(a,b:String; c:Int){
                obj.a = 5;
            }
        }
        """
        expect = "Undeclared Identifier: obj"
        self.assertTrue(TestChecker.test(input,expect,30))

    def test31(self):
        input ="""
        Class A{
            Var b:Int;

            getName(a,b:String; c:Int){
                (New A()).a = 5;
            }
        }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,31))

    def test30(self):
        input ="""
        Class A{
            Var a:Int;
            $a(){
                Return;
            }
            getName(a,b:String; c:Int){
                Var array:Array[Int,2] = Array(1,2);
                Var e:Int = 5;
                array[e] = A::$a();
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(array),[Id(e)]),CallExpr(Id(A),Id($a),[]))"
        self.assertTrue(TestChecker.test(input,expect,30))

    def test31(self):
        input ="""
        Class A{
            Var a:Array[Int,5] = Array(1,2,3,4,5);
            method(){
                Val b: Int = Self.a[0];
            }
        }
        Class Program{
            main(){

            }
        }
        """
        expect = "Illegal Constant Expression: ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(0)])"
        self.assertTrue(TestChecker.test(input,expect,31))

    def test32(self):
        input ="""
        Class B{
            Constructor(a,b:String){
                Return;
            }
            Destructor(){
                Return;
            }
        }
        Class A{
            Method(a,b:B){
                Return Array("Hello","Hi");
            }
            Val a:Array[Int,5] = Array(1,2,3,4,5);
            method(){
                Val b: Int = Self.a[0];
                Var a:Array[Int,2] = Array(1,34);
                Val obj: B = New B("Hello", "Hello");
                Var arr:Array[Float, 2];
                arr = Self.Method(New B("Hello", "Hello"), obj);
            }
        }
        Class Program{
            main(){

            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(arr),CallExpr(Self(),Id(Method),[NewExpr(Id(B),[StringLit(Hello),StringLit(Hello)]),Id(obj)]))"
        self.assertTrue(TestChecker.test(input,expect,32))

    def test33(self):
        input ="""
        Class A{
            method(){
                Return 1;
            }
            main(a,b:String; c:String){
                Val obj: A = New A();
                Self.method();
            }
        }
        Class Program{
            main(){

            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Self(),Id(method),[])"
        self.assertTrue(TestChecker.test(input,expect,33))

    def test34(self):
        input ="""
        Class C{
            Var c:Int = 5;
        }
        Class B{
            Val c:C = New C();
        }
        Class A:B{
            Var att:Int = 5;
            Var b:B = New B();
            att(){}
            method(){
                Var obj: B= New B();
                Self.att = obj.c.c + 1;
                Var a:Int = 1;
                Foreach(a In obj.c.c .. obj.c.c){
                    Var arr: Array[Boolean,5];
                    If (arr[0]){
                        Self.att = 1;
                        Self.att = Self.att() + 5;
                    }
                }
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(att),[])"
        self.assertTrue(TestChecker.test(input,expect,34))

    def test35(self):
        input ="""
        Class A{
            Val $a:Int = 5;
        }
        Class Program{
            program(){
                Var a:A = New A();
                Var arr: Array[Boolean,4];
                If(arr[0]){
                    Return A::$a;
                } Else{
                    Val c:Int = 6;
                    {
                        Return c;
                    }
                    Return 5;
                }
                Return 7;
                c = c + 1;
            }
            main(){
                Return;
            }

        }

        """
        expect = """Undeclared Identifier: c"""
        self.assertTrue(TestChecker.test(input,expect,35))

    def test36(self):
        input = """
        Class A{}
        Class Program{
            main(){
                Return;
            }
        }
        Class B:A{
            Var x:String;
            x(){}
            Var a:Int;
            Var b:Int;
            Var c:Int;
            x(){}
            Var x:String;

        }
        """
        expect = "Redeclared Method: x"
        self.assertTrue(TestChecker.test(input, expect,36))

    def test37(self):
        input = """
        Class Program{
            main(){
                Return;
            }
        }
        Class A{
            method(){
                Var i: Int = 1;
                Foreach( i In 1 .. 100){
                    Return "hi";
                }
                If (True){
                    Return "String";
                } Elseif(False){
                    Return "Hello";
                }
            Return i;
            }
        }
        """
        expect= "Type Mismatch In Statement: Return(Id(i))"
        self.assertTrue(TestChecker.test(input, expect,37))

    def test38(self):
        input = """
        Class Program{
            main(){
                Var i: Int = 1;
                Foreach( i In 1 .. 100){
                    Return ;
                }
                If (True){
                    Return ;
                } Elseif(False){
                    Return ;
                }
            Return i;
            }
        }
        Class A{
            method(){

            }
        }
        """
        expect= "Type Mismatch In Statement: Return(Id(i))"
        self.assertTrue(TestChecker.test(input, expect,38))

    def test39(self):
        input = """
        Class Program{
            main(){
                Var i: Int = 1;
                Foreach( i In 1 .. 100){
                    Return ;
                }
                If (True){
                    Return ;
                } Elseif(False){
                    Return ;
                }
            Return;
            }
        }
        Class A{
            main(){
               Return "Hello";
            }
        }
        """
        expect= "[]"
        self.assertTrue(TestChecker.test(input, expect,39))

    def test40(self):
        input = """
        Class Program{
            main(){
                Var i: Int = 1;
                Foreach( i In 1 .. 100){
                    Return ;
                }
                If (True){
                    Return ;
                } Elseif(False){
                    Return ;
                }
            Return;
            }
        }
        Class A{
            main(){
               Return "Hello";
            }
            method(){
                Val a:Float = (1 +2.0 - 2) / 4.0 * 5;
                Val b:Int = 1%2;
                Val c:Boolean = "String" ==. "Hello";
                Val f:Boolean = "String" ==. "Hello";
                Val d:String = "String" +. "Hello";
                Var e:Boolean = (!c || f) && c ;
            }
        }

        """
        expect= "[]"
        self.assertTrue(TestChecker.test(input, expect,40))

    def test41(self):
        input = """
        Class B{
            Constructor(a,b:Int; c:String){
                Return;
            }
            Val b:B = New B(1,2,"Hoang");
            Val c:B = Self.b;
            Var $c:B = Self.c;
        }
        Class Program{
            main(){
                Val b:B = New B(1,2,"Hoang").c;
                {
                    Val b: B = B::$c;
                    {
                        B::$c = b.c;
                        B::$c = b;
                        B::$c = b.b;
                        Val b: B = New B(1,2.0);
                    }
                }
                Return;
            }
        }

        Class A{
            main(){
                Return 1;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect,41))

    def test42(self):
        input = """
                Class Program{
                    main() { 
                        Return;
                    }
                }

               Class A {
                   Var $a: Int = 5;
                   Var kk: Int = 5;
                   Var ss: String = "Bug";
                   A(){
                       Return 1;
                   }
                   Var A:Int = 1;
               }

               Class C{
                   Var x, y: Int = 4, 5;
                   Var tmp: Float;
                   A(){
                       Return 1;
                   }
                   Val A:Int = 1;

                   method(){
                        Var A: A;
                        Self.tmp = A.kk + 12;
                        A.ss = "yeyeye";
                        Self.tmp = A::$a + 10;
                        A::$a = A.kk + 12 + Self.A() + Self.A - A.A() + A.A;
                   }
               }

                """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 42))

    def test43(self):
        input = """
        Class B{
            Val a:Int = 5;
        }
        Class A:B{
            Constructor(a: Array[Int,2]; b:String; c:B){
            }
        }   
        Class Program{
            main(){
                Val obj:A = New A(Array(1,2), "Hello", New B());
                Return;
            }
        }

        Class C:D{

        }
        """
        expect = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(input, expect, 43))

    def test44(self):
        input = """
            Class A{
                Var a: Array[Array[Int,2], 3] = Array(Array(1,2), Array(3,4), Array(5,6));
                Var b: Array[Array[Int,2], 3] = Array(Array(1,2,3), Array(3,4), Array(5,6));
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Illegal Array Literal: [[IntLit(1),IntLit(2),IntLit(3)],[IntLit(3),IntLit(4)],[IntLit(5),IntLit(6)]]"
        self.assertTrue(TestChecker.test(input, expect, 44))

    def test45(self):
        input = """
            Class A{
                Val a: Array[Array[Array[String,2], 3], 1] = Array(Array(Array("khang", "best"), Array("heo","ngu"), Array("Hana", "cute")));
                Var b: Array[Array[Array[String,2], 3], 1] = Array(Array(Array("1", "best"), Array("heo","ngu"), Array("khang", "pro")));
                Var c: Array[Float, 4] = Array(5.67, 1e10, 6.890, 2.5e-10);
                Var d: Array[Array[Int,2], 3] = Array(Array(1,2), Array(3,4), Array(5,6), Array(7,8));
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Type Mismatch In Constant Declaration: AttributeDecl(Instance,VarDecl(Id(d),ArrayType(3,ArrayType(2,IntType)),[[IntLit(1),IntLit(2)],[IntLit(3),IntLit(4)],[IntLit(5),IntLit(6)],[IntLit(7),IntLit(8)]]))"
        self.assertTrue(TestChecker.test(input, expect, 45))

    def test46(self):
        input = """
        Class A{
            Val method:Int = 1;
            Var method_:Int = 5;
            method(){
                Return 1;
            }
            Val a:Int = Self.method();
            main(){
                Val a:Int = Self.method;
                Val b:Int = Self.method;
            }

        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Illegal Constant Expression: CallExpr(Self(),Id(method),[])"
        self.assertTrue(TestChecker.test(input, expect, 46))

    def test47(self):
        input = """
        Class A{
            method(){
                Val a: Array[Array[Int,2], 2] = Array(Array(1,2), Array(1,2));
                Var b:Int = a[0][1];
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 47))

    def test48(self):
        input = """
            Class A{
                Val a: Array[Array[String,1],2] = Array(Array("a"), Array("b"));
                Val b: Array[Array[Array[Int,1],1],1] = Array(Array(Array(1)));
                Var c: Array[Array[Array[Float,1],1],1] = Array(Array(Array(1.0)));
                Var d: Array[Array[Array[Array[Float, 1],1],1],1] = Array(Array(Array(Array(1.0))));

                program(){
                    Val a:String = Self.a[0][0];
                    Val b:Int = Self.b[0][0][0];
                    Self.c[0][0][0] = Self.b[0][0][0];
                    Self.c[0] = Self.d[0][0];
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 48))

    def test49(self):
        input = """
            Class A{
                Val a: Array[Array[String,1],2] = Array(Array("a"), Array("b"));
                Val b: Array[Array[Array[Int,1],1],1] = Array(Array(Array(1)));
                Val $b: Array[Array[Array[Int,1],1],1] = Array(Array(Array(1)));
                Var c: Array[Array[Array[Float,1],1],1] = Array(Array(Array(1.0)));
                Var d: Array[Array[Array[Array[Float, 1],1],1],1] = Array(Array(Array(Array(1.0))));

                Constructor(a: Array[Array[Int,1],1]; b:Int){
                    Return;
                }

                program(){
                    Var o: Array[Array[Int,1],1] = Self.b[0];
                    Val obj: A = New A(Self.b[0], A::$b[0][0][0]);
                    Val a:String = obj.a[0][0]; 
                }
                Destructor(){
                    Return;
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 49))

    def test48(self):
        input = """
            Class A{
                Val a: Array[Array[String,1],2] = Array(Array("a"), Array("b"));
                Val b: Array[Array[Array[Int,1],1],1] = Array(Array(Array(1)));
                Var c: Array[Array[Array[Float,1],1],1] = Array(Array(Array(1.0)));
                Var d: Array[Array[Array[Array[Float, 1],1],1],1] = Array(Array(Array(Array(1.0))));

                program(){
                    Val a:String = Self.a[0][0];
                    Val b:Int = Self.b[0][0][0];
                    Self.c[0][0][0] = Self.b[0][0][0];
                    Self.c[0] = Self.d[0][0];
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 48))

    def test49(self):
        input = """
            Class A{
                Val a: Array[Array[String,1],2] = Array(Array("a"), Array("b"));
                Val b: Array[Array[Array[Int,1],1],1] = Array(Array(Array(1)));
                Var c: Array[Array[Array[Float,1],1],1] = Array(Array(Array(1.0)));
                Var d: Array[Array[Array[Array[Float, 1],1],1],1] = Array(Array(Array(Array(1.0))));

                program(){
                    Val a:String = Self.a[0][0];
                    Val b:Int = Self.b[0][0][0];
                    Self.c[0][0][0] = Self.b[0][0][0];
                    Self.c[0] = Self.d[0][0];
                }
            }
            Class Program{
                main(){
                }
            }
             """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 49))

    def test50(self):
        input = """
            Class B{
                $method(){
                    Return "Hello";
                }
            }
            Class A:B{

                program(){
                    Val a: String = "Hello" +. B::$method();
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Illegal Constant Expression: BinaryOp(+.,StringLit(Hello),CallExpr(Id(B),Id($method),[]))"
        self.assertTrue(TestChecker.test(input, expect, 50))

    def test51(self):
        input = """
            Class A{

                program(){
                    Var a:Int = 5;
                    Val b: Int  =  1 + a + a + 5; 
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Illegal Constant Expression: BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),Id(a)),Id(a)),IntLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 51))

    def test52(self):
        input = """
            Class B{
                Var a:Array[Array[String,1],1];
            }
            Class A{
                Var a:B;
                Constructor(a:Array[String, 1]){

                }

                program(){
                    Var obj: A = New A(Self.a.a[0]);
                }
            }
            Class Program{
                main(){
                }
            }
             """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 52))

    def test53(self):
        input = """
            Class B{
                Val a:Array[Array[String,1],1] = Array(Array("b"));
            }
            Class A{
                Val a:B = New B();
                Constructor(a:Array[String, 1]){

                }

                program(){
                    Var obj: A = New A(Self.a.a[0]);
                }
            }
            Class Program{
                main(){
                }
            }
             """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 53))

    def test54(self):
        input = """
            Class B{
                Val a:Array[Array[String,1],1] = Array(Array("a"));
            }
            Class A{
                Val a:B = New B();
                Constructor(a:Array[String, 1]){

                }

                program(){
                    Val obj: A = New A(Self.a.a[0]);
                }
            }
            Class Program{
                main(){
                }
            }
             """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 54))

    def test55(self):
        input = """
            Class A{
                Val a: Int;

                program(){

                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Undeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 55))

    def test56(self):
        input = """
            Class A{
                Val a: A;

                program(){

                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Undeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 56))

    def test57(self):
        input = """
            Class A{

                program(){
                    Val a: Int;
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Undeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 57))

    def test58(self):
        input = """
            Class A{

                program(){
                    Val a: A;
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Undeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 58))

    def test59(self):
        input = """
            Class A{
                main(){
                    Var a: Int = 1;
                    {
                        Var b:Array[Int,5] = Array(1,2,3,4,5);
                        a = b[0];
                        {
                            b[0] = a;
                            b[0] = b[1];
                        }
                    }
                }

            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 59))

    def test60(self):
        input = """
            Class B{
                main(){
                    Return "Hello";
                }
            }
            Class A{

                program(){
                    Return;
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 60))

    def test61(self):
        input = """
            Class A{
                program(){
                }

                program_(){
                    Return;
                }

                main(){
                    Val a: A = New A();
                    a.program();
                    a.program_();
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 61))

    def test62(self):
        input = """
            Class A{
                Var $a:Int = 5;
                Val $b: Int = 6;
                program(){
                    Val a:A = New A();
                    a::$a = a::$a;
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Undeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 62))

    def test63(self):
        input = """
            Class A{
                Var $a:Int = 5;
                Val $b: Int = 6;
                Val a:Int = 5;
                program(){
                    Val a:A = New A();
                    A::$a = A::$a;
                    A.a = 5;
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Illegal Member Access: FieldAccess(Id(A),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 62))

    def test63(self):
        input = """
           Class A{
                Var $a:Int = 5;
                Val $b: Int = 6;
                Val a:Int = 5;
                program(){
                    Val a:A = New A();
                    A::$a = A::$a;
                    obj.a = 5;
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Undeclared Identifier: obj"
        self.assertTrue(TestChecker.test(input, expect, 63))

    def test64(self):
        input = """
            Class A{
                Var $a:Int = 5;
                Val $b: Int = 6;
                Val a:Int = 5;
                program(){
                    Val a:A = New A();
                    Val obj:A = New A();
                    A::$a = A::$a;
                    obj.att = 5;
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
            """
        expect = "Undeclared Attribute: att"
        self.assertTrue(TestChecker.test(input, expect, 64))

    def test65(self):
        input = """
            Class A{
                Var $a:Int = 5;
                Val $b: Int = 6;
                Val a:Int = 5;
                method(){

                }
                program(){
                    Val a:A = New A();
                    Val obj:A = New A();
                    A::$a = A::$a;
                    Val c:Int= obj.method_();
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
            """
        expect = "Undeclared Method: method_"
        self.assertTrue(TestChecker.test(input, expect, 65))

    def test66(self):
        input = """
            Class A{
                Var $a:Int = 5;
                Val $b: Int = 6;
                Val a:Int = 5;
                method(){

                }
                program(){
                    Val a:A = New A();
                    Val obj:A = New A();
                    A::$a = A::$a;
                    Val c:Int= obj.method();
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Type Mismatch In Expression: CallExpr(Id(obj),Id(method),[])"
        self.assertTrue(TestChecker.test(input, expect, 66))

    def test67(self):
        input = """
            Class A{
                Var $a:Int = 5;
                Val $b: Int = 6;
                Val a:Int = 5;
                method(){
                    Return 1;
                }
                program(){
                    Val a:A = New A();
                    Val obj:A = New A();
                    A::$a = A::$a;
                    Val c:Int= obj.method();
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Illegal Constant Expression: CallExpr(Id(obj),Id(method),[])"
        self.assertTrue(TestChecker.test(input, expect, 67))

    def test68(self):
        input = """
            Class A{
                Val c:Array[Array[Int,1],1] = Array(Array(1))
                Val b:Int = Self.c[0][0];
                Val a:Int = Self.b;
                program(){
                    Val a:Int = Self.a;
                }
            }
            Class Program{
                main(){
                    Return;
                }
            }
             """
        expect = "Undeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 68))

    def test69(self):
        input = """
            Class A{
                Val a:Boolean = True;
            }
            Class B{
                Val a:A = New A();
            }
            Class C{
                Val a:B = New B();
            }
            Class Program(){
                main(){
                    Return;
                    Val obj:C = New C();

                    If(obj.a.a.a){

                    } Else{

                    }
                }
            }
            """
        expect = "Undeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 69))

    def test70(self):
        input = """
            Class Program{
                main(){
                    Return;
                }
            }
            Class Base{
                Var $a:Int = 5;
            }
            Class A:Base{
                method(){
                    A::$a = 5;   
                }
            }
             """
        expect = "Undeclared Attribute: $a"
        self.assertTrue(TestChecker.test(input, expect, 70))

    def test71(self):
        input = """
            Class A{
                $method(){
                    Return 1;
                }
            }
            Class B{
                $method(){
                    Return A::$method();
                }
            }
            Class C{
                $method(){
                    Return B::$method();
                }
            }
            Class Program(){
                main(){
                    Return;
                    Var a:Int = C::$method();
                }
            }
             """
        expect = "Undeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 72))

    def test72(self):
        input = """
            Class Program(){
                main(){
                    {
                        Var i:Int = 5;
                        Foreach(i In 1 .. 100){
                            Break;
                            {
                                Break;
                            }
                        }
                        {
                            Break;
                        }
                    }
                    Return;
                }
            }
             """
        expect = "Undeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 72))

    def test73(self):
        input = """
            Class A{
                $method(){
                    Return 1;
                }
            }
            Class B{
                $method(){
                    Return A::$method();
                }
            }
            Class C{
                $method(){
                    Return B::$method();
                }
            }
            Class Program(){
                method(){
                    If(True){
                        Return C::$method();
                    } Else{
                        Return 1;
                    }
                }
                main(){
                    Return;
                }
            }
             """
        expect = "Undeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 73))

    def test74(self):
        input = """
            Class A{

            }
            Class Program:A{
                main(){
                    Return;
                }
            }
            Class C:D{

            }
             """
        expect = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(input, expect, 74))

    def test75(self):
        input = """
            Class A{
                Val a:Boolean = True;
            }

            Class Program{
                main(){
                    Return;
                    Var a:Int = C::$a;
                }
            }
             """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 75))

    def test76(self):
        input = """
            Class A{

            }
            Class B{
                main(){
                    Var a:Array[Array[Int,1],1];
                    Var b:Array[Array[Float,1],1];
                    Var c:Float = a[0][0] + b[0][0];
                    Var d:Array[Array[String,1],1];
                    Var e:Boolean = d[0][0] ==. "Hello";
                    Var f:Float = a[0][0] + b[0][0] - c / a[0][0] * b[0];
                    Var g:Boolean = 1 > 5;
                    Var w:Boolean = g && e || g;
                    b = -a;
                }
            }
            """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 76))

    def test77(self):
        input = """
            Class Program{
                main(){
                    Val c:Int = 5;
                    c = c[0];
                    Return;
                }
            }
             """
        expect = "Cannot Assign To Constant: AssignStmt(Id(c),ArrayCell(Id(c),[IntLit(0)]))"
        self.assertTrue(TestChecker.test(input, expect, 77))

    def test78(self):
        input = """
            Class A{
                Val a:Array[Int,5] = Array(1,2,3,4,5);
            }
            Class B{
                Val a:A = New A();
            }
            Class C{
                Val a:B = New B();
            }
            Class Program{
                main(){
                    Return;
                    Var obj:C = New C();
                    Val a:Int = obj.a.a.a[0];

                }
            }
             """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 78))

    def test79(self):
        input = """
            Class A{
                Var a:Array[Int,5] = Array(1,2,3,4,5);
            }
            Class B{
                Var a:A = New A();
            }
            Class C{
                Var a:B = New B();
            }
            Class Program{
                main(){
                    Return;
                    Var obj:C = New C();
                    obj.a.a.a[0] = obj.a.a.a[0] + 1 / 2 ;

                }
            }
             """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 79))

    def test80(self):
        input = """
            Class A{
                Destructor(){
                    Return;
                }
            }
            Class Program{
                main(){

                }
            }
            """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 80))

    def test81(self):
        input = """
        Class Program {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 81))

    def test82(self):
        input = """
        Class Program {
            main(a: Int) {}
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 82))

    def test83(self):
        input = """
        Class A {
            Val a: A = New A();
        }
        Class Program {
            main() {
                Val a: A = New A().a;
                New A().a = a;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(NewExpr(Id(A),[]),Id(a)),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 83))

    def test84(self):
        input = """
        Class Program {
            main() {
                Val a: Int = 5.5;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 84))

    def test85(self):
        input = """
        Class Program{
            main() {
                Val a: Int;
            }
        }
        """
        expect = "Undeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 85))

    def test86(self):
        input = """
        Class Program {
            main() {
                Var a: Int;
                a = 5.5;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),FloatLit(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 86))

    def test87(self):
        input = """
        Class Program {
            Var a: Float;
            main() {
                Var a: Int;
                Self.a = 10;
                a = 5 + 5.5;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLit(5),FloatLit(5.5)))"
        self.assertTrue(TestChecker.test(input, expect, 87))

    def test88(self):
        input = """
        Class Program {
            Var a: Float;
            main() {
                Var a: Int;
                Self.a = 10;
                a = 5 + 5.5;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLit(5),FloatLit(5.5)))"
        self.assertTrue(TestChecker.test(input, expect, 88))

    def test89(self):
        input = """
        Class Program {
            Var a: Float;
            main() {
                Self.a = 10;
                a = 5 + 5.5;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 89))

    def test90(self):
        input = """
        Class Program {
            Var a: Float;
            main() {
                Self.b = 10;
            }
        }
        """
        expect = "Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 90))

    def test_11(self):
        input = """
        Class B : A{}
        Class Program {
            Var a: Float;
            main() {
                Self.a = 10;
            }
        }
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, "Test_11"))

    def test91(self):
        input = """
        Class Program {
            Val a: Float = 5;
            main() {
                Self.a();
            }
        }
        """
        expect = "Undeclared Method: a"
        self.assertTrue(TestChecker.test(input, expect, 91))

    def test92(self):
        input = """
        Class Program {
            Val a: Float = 5;
            main() {
                Var a: Program;
                a.a = 10;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(a),Id(a)),IntLit(10))"
        self.assertTrue(TestChecker.test(input, expect, 92))

    def test93(self):
        input = """
        Class Program {
            Var a: Float;
            a(a: Int) {
                Return Self.a;
            }
            main(){}
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 93))

    def test94(self):
        input = """
        Class Program {
            a(a: Int) {
                Var a: Float;
            }
            main(){}
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 94))

    def test95(self):
        input = """
        Class Program {}
        Class Program {
            a(a: Int) {
            }
            main(){}
        }
        """
        expect = "Redeclared Class: Program"
        self.assertTrue(TestChecker.test(input, expect, 95))

    def test96(self):
        input = """
        Class Program {
            a(a: Int) {}
            Var a: Float;
            main(){}
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 96))

    def test97(self):
        input = """
        Class Program {
            a(a: Int; a: Float) {}
            main(){}
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 97))

    def test98(self):
        input = """
        Class Program {
            a(a: Int) {
                Val a: Float = 5.5;
            }
            main(){}
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 98))

    def test99(self):
        input = """
        Class Program {
            a(a: Int) {
                Var b: Int = 5;
                Val c: Float = 5.5e3;
                b = 1 + c;
            }
            main(){}
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),BinaryOp(+,IntLit(1),Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 99))

    def test100(self):
        input = """
        Class Program {
            a(a: Int) {
                Var b: String = "Hello ";
                b = b + a;
            }
            main(){}
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input, expect,100))
