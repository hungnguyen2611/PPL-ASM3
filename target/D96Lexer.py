# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0231\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\39\39\59\u017d\n9\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\5:\u018a\n:\3;\3;\5;\u018e\n;\3;\7;\u0191\n;\f;\16;")
        buf.write("\u0194\13;\3<\6<\u0197\n<\r<\16<\u0198\3=\3=\3=\5=\u019e")
        buf.write("\n=\3=\7=\u01a1\n=\f=\16=\u01a4\13=\3>\3>\3>\3>\5>\u01aa")
        buf.write("\n>\3>\7>\u01ad\n>\f>\16>\u01b0\13>\3?\3?\3?\3?\5?\u01b6")
        buf.write("\n?\3?\7?\u01b9\n?\f?\16?\u01bc\13?\3@\3@\5@\u01c0\n@")
        buf.write("\3@\3@\5@\u01c4\n@\3@\3@\3@\3@\3@\5@\u01cb\n@\3@\5@\u01ce")
        buf.write("\n@\3@\3@\3A\3A\7A\u01d4\nA\fA\16A\u01d7\13A\3A\3A\3A")
        buf.write("\3A\3B\3B\5B\u01df\nB\3B\3B\3C\3C\5C\u01e5\nC\3D\3D\3")
        buf.write("E\3E\3F\3F\7F\u01ed\nF\fF\16F\u01f0\13F\3G\3G\6G\u01f4")
        buf.write("\nG\rG\16G\u01f5\3H\3H\3H\3H\7H\u01fc\nH\fH\16H\u01ff")
        buf.write("\13H\3H\3H\3H\3H\3H\3I\6I\u0207\nI\rI\16I\u0208\3I\3I")
        buf.write("\3J\3J\3J\3J\5J\u0211\nJ\3K\3K\3K\3L\3L\3L\3M\3M\7M\u021b")
        buf.write("\nM\fM\16M\u021e\13M\3M\5M\u0221\nM\3M\3M\3N\3N\7N\u0227")
        buf.write("\nN\fN\16N\u022a\13N\3N\3N\3N\3O\3O\3O\3\u01fd\2P\3\3")
        buf.write("\5\2\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33")
        buf.write("\16\35\17\37\20!\21#\22%\23\'\24)\25+\26-\27/\30\61\31")
        buf.write("\63\32\65\33\67\349\35;\36=\37? A!C\"E#G$I%K&M\'O(Q)S")
        buf.write("*U+W,Y-[.]/_\60a\61c\62e\63g\64i\65k\2m\66o\67q8s9u\2")
        buf.write("w\2y\2{\2}\2\177:\u0081;\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b<\u008d=\u008f>\u0091?\u0093\2\u0095\2\u0097\2")
        buf.write("\u0099@\u009bA\u009dB\3\2\27\4\2DDdd\4\2ZZzz\3\2\63;\3")
        buf.write("\2\62\62\3\2\639\3\2\629\4\2\63;CH\4\2\62;CH\3\2\63\63")
        buf.write("\3\2\62\63\3\2$$\4\2GGgg\3\2\62;\4\2--//\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\5\2\13\f\17\17\"\"\3\2))\5\2\f\f$$^^\t\2")
        buf.write("))^^ddhhppttvv\3\3\f\f\2\u0241\2\3\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\3\u009f\3\2\2\2\5\u00a5\3\2\2\2\7\u00a7\3\2\2\2\t\u00ac")
        buf.write("\3\2\2\2\13\u00b2\3\2\2\2\r\u00bb\3\2\2\2\17\u00c2\3\2")
        buf.write("\2\2\21\u00c5\3\2\2\2\23\u00cc\3\2\2\2\25\u00d1\3\2\2")
        buf.write("\2\27\u00d9\3\2\2\2\31\u00dc\3\2\2\2\33\u00e1\3\2\2\2")
        buf.write("\35\u00e7\3\2\2\2\37\u00ec\3\2\2\2!\u00f0\3\2\2\2#\u00f6")
        buf.write("\3\2\2\2%\u00fe\3\2\2\2\'\u0105\3\2\2\2)\u010b\3\2\2\2")
        buf.write("+\u0117\3\2\2\2-\u0122\3\2\2\2/\u0126\3\2\2\2\61\u0129")
        buf.write("\3\2\2\2\63\u012d\3\2\2\2\65\u0131\3\2\2\2\67\u0133\3")
        buf.write("\2\2\29\u0136\3\2\2\2;\u0139\3\2\2\2=\u013d\3\2\2\2?\u0140")
        buf.write("\3\2\2\2A\u0142\3\2\2\2C\u0144\3\2\2\2E\u0146\3\2\2\2")
        buf.write("G\u0148\3\2\2\2I\u014a\3\2\2\2K\u014d\3\2\2\2M\u0150\3")
        buf.write("\2\2\2O\u0152\3\2\2\2Q\u0154\3\2\2\2S\u0157\3\2\2\2U\u015a")
        buf.write("\3\2\2\2W\u015c\3\2\2\2Y\u015e\3\2\2\2[\u0160\3\2\2\2")
        buf.write("]\u0162\3\2\2\2_\u0164\3\2\2\2a\u0166\3\2\2\2c\u0168\3")
        buf.write("\2\2\2e\u016a\3\2\2\2g\u016d\3\2\2\2i\u016f\3\2\2\2k\u0172")
        buf.write("\3\2\2\2m\u0174\3\2\2\2o\u0176\3\2\2\2q\u017c\3\2\2\2")
        buf.write("s\u0189\3\2\2\2u\u018b\3\2\2\2w\u0196\3\2\2\2y\u019a\3")
        buf.write("\2\2\2{\u01a5\3\2\2\2}\u01b1\3\2\2\2\177\u01cd\3\2\2\2")
        buf.write("\u0081\u01d1\3\2\2\2\u0083\u01dc\3\2\2\2\u0085\u01e2\3")
        buf.write("\2\2\2\u0087\u01e6\3\2\2\2\u0089\u01e8\3\2\2\2\u008b\u01ea")
        buf.write("\3\2\2\2\u008d\u01f1\3\2\2\2\u008f\u01f7\3\2\2\2\u0091")
        buf.write("\u0206\3\2\2\2\u0093\u0210\3\2\2\2\u0095\u0212\3\2\2\2")
        buf.write("\u0097\u0215\3\2\2\2\u0099\u0218\3\2\2\2\u009b\u0224\3")
        buf.write("\2\2\2\u009d\u022e\3\2\2\2\u009f\u00a0\7E\2\2\u00a0\u00a1")
        buf.write("\7n\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a4")
        buf.write("\7u\2\2\u00a4\4\3\2\2\2\u00a5\u00a6\7&\2\2\u00a6\6\3\2")
        buf.write("\2\2\u00a7\u00a8\7U\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa")
        buf.write("\7n\2\2\u00aa\u00ab\7h\2\2\u00ab\b\3\2\2\2\u00ac\u00ad")
        buf.write("\7D\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7g\2\2\u00af\u00b0")
        buf.write("\7c\2\2\u00b0\u00b1\7m\2\2\u00b1\n\3\2\2\2\u00b2\u00b3")
        buf.write("\7E\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9")
        buf.write("\7w\2\2\u00b9\u00ba\7g\2\2\u00ba\f\3\2\2\2\u00bb\u00bc")
        buf.write("\7T\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7w\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7p\2\2\u00c1\16")
        buf.write("\3\2\2\2\u00c2\u00c3\7K\2\2\u00c3\u00c4\7h\2\2\u00c4\20")
        buf.write("\3\2\2\2\u00c5\u00c6\7G\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8")
        buf.write("\7u\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7h\2\2\u00cb\22\3\2\2\2\u00cc\u00cd\7G\2\2\u00cd\u00ce")
        buf.write("\7n\2\2\u00ce\u00cf\7u\2\2\u00cf\u00d0\7g\2\2\u00d0\24")
        buf.write("\3\2\2\2\u00d1\u00d2\7H\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7t\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7")
        buf.write("\7e\2\2\u00d7\u00d8\7j\2\2\u00d8\26\3\2\2\2\u00d9\u00da")
        buf.write("\7K\2\2\u00da\u00db\7p\2\2\u00db\30\3\2\2\2\u00dc\u00dd")
        buf.write("\7V\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7w\2\2\u00df\u00e0")
        buf.write("\7g\2\2\u00e0\32\3\2\2\2\u00e1\u00e2\7H\2\2\u00e2\u00e3")
        buf.write("\7c\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5\7u\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6\34\3\2\2\2\u00e7\u00e8\7P\2\2\u00e8\u00e9")
        buf.write("\7w\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7n\2\2\u00eb\36")
        buf.write("\3\2\2\2\u00ec\u00ed\7K\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7v\2\2\u00ef \3\2\2\2\u00f0\u00f1\7H\2\2\u00f1\u00f2")
        buf.write("\7n\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5\"\3\2\2\2\u00f6\u00f7\7D\2\2\u00f7\u00f8")
        buf.write("\7q\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7p\2\2\u00fd$\3")
        buf.write("\2\2\2\u00fe\u00ff\7U\2\2\u00ff\u0100\7v\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7k\2\2\u0102\u0103\7p\2\2\u0103\u0104")
        buf.write("\7i\2\2\u0104&\3\2\2\2\u0105\u0106\7C\2\2\u0106\u0107")
        buf.write("\7t\2\2\u0107\u0108\7t\2\2\u0108\u0109\7c\2\2\u0109\u010a")
        buf.write("\7{\2\2\u010a(\3\2\2\2\u010b\u010c\7E\2\2\u010c\u010d")
        buf.write("\7q\2\2\u010d\u010e\7p\2\2\u010e\u010f\7u\2\2\u010f\u0110")
        buf.write("\7v\2\2\u0110\u0111\7t\2\2\u0111\u0112\7w\2\2\u0112\u0113")
        buf.write("\7e\2\2\u0113\u0114\7v\2\2\u0114\u0115\7q\2\2\u0115\u0116")
        buf.write("\7t\2\2\u0116*\3\2\2\2\u0117\u0118\7F\2\2\u0118\u0119")
        buf.write("\7g\2\2\u0119\u011a\7u\2\2\u011a\u011b\7v\2\2\u011b\u011c")
        buf.write("\7t\2\2\u011c\u011d\7w\2\2\u011d\u011e\7e\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7q\2\2\u0120\u0121\7t\2\2\u0121,\3")
        buf.write("\2\2\2\u0122\u0123\7P\2\2\u0123\u0124\7g\2\2\u0124\u0125")
        buf.write("\7y\2\2\u0125.\3\2\2\2\u0126\u0127\7D\2\2\u0127\u0128")
        buf.write("\7{\2\2\u0128\60\3\2\2\2\u0129\u012a\7X\2\2\u012a\u012b")
        buf.write("\7c\2\2\u012b\u012c\7t\2\2\u012c\62\3\2\2\2\u012d\u012e")
        buf.write("\7X\2\2\u012e\u012f\7c\2\2\u012f\u0130\7n\2\2\u0130\64")
        buf.write("\3\2\2\2\u0131\u0132\7#\2\2\u0132\66\3\2\2\2\u0133\u0134")
        buf.write("\7(\2\2\u0134\u0135\7(\2\2\u01358\3\2\2\2\u0136\u0137")
        buf.write("\7~\2\2\u0137\u0138\7~\2\2\u0138:\3\2\2\2\u0139\u013a")
        buf.write("\7?\2\2\u013a\u013b\7?\2\2\u013b\u013c\7\60\2\2\u013c")
        buf.write("<\3\2\2\2\u013d\u013e\7-\2\2\u013e\u013f\7\60\2\2\u013f")
        buf.write(">\3\2\2\2\u0140\u0141\7-\2\2\u0141@\3\2\2\2\u0142\u0143")
        buf.write("\7/\2\2\u0143B\3\2\2\2\u0144\u0145\7,\2\2\u0145D\3\2\2")
        buf.write("\2\u0146\u0147\7\61\2\2\u0147F\3\2\2\2\u0148\u0149\7\'")
        buf.write("\2\2\u0149H\3\2\2\2\u014a\u014b\7?\2\2\u014b\u014c\7?")
        buf.write("\2\2\u014cJ\3\2\2\2\u014d\u014e\7#\2\2\u014e\u014f\7?")
        buf.write("\2\2\u014fL\3\2\2\2\u0150\u0151\7>\2\2\u0151N\3\2\2\2")
        buf.write("\u0152\u0153\7@\2\2\u0153P\3\2\2\2\u0154\u0155\7>\2\2")
        buf.write("\u0155\u0156\7?\2\2\u0156R\3\2\2\2\u0157\u0158\7@\2\2")
        buf.write("\u0158\u0159\7?\2\2\u0159T\3\2\2\2\u015a\u015b\7?\2\2")
        buf.write("\u015bV\3\2\2\2\u015c\u015d\7*\2\2\u015dX\3\2\2\2\u015e")
        buf.write("\u015f\7+\2\2\u015fZ\3\2\2\2\u0160\u0161\7}\2\2\u0161")
        buf.write("\\\3\2\2\2\u0162\u0163\7\177\2\2\u0163^\3\2\2\2\u0164")
        buf.write("\u0165\7=\2\2\u0165`\3\2\2\2\u0166\u0167\7<\2\2\u0167")
        buf.write("b\3\2\2\2\u0168\u0169\7.\2\2\u0169d\3\2\2\2\u016a\u016b")
        buf.write("\7\60\2\2\u016b\u016c\7\60\2\2\u016cf\3\2\2\2\u016d\u016e")
        buf.write("\7\60\2\2\u016eh\3\2\2\2\u016f\u0170\5a\61\2\u0170\u0171")
        buf.write("\5a\61\2\u0171j\3\2\2\2\u0172\u0173\7a\2\2\u0173l\3\2")
        buf.write("\2\2\u0174\u0175\7]\2\2\u0175n\3\2\2\2\u0176\u0177\7_")
        buf.write("\2\2\u0177p\3\2\2\2\u0178\u017d\5u;\2\u0179\u017d\5y=")
        buf.write("\2\u017a\u017d\5{>\2\u017b\u017d\5}?\2\u017c\u0178\3\2")
        buf.write("\2\2\u017c\u0179\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017b")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\b9\2\2\u017f")
        buf.write("r\3\2\2\2\u0180\u018a\7\62\2\2\u0181\u0182\7\62\2\2\u0182")
        buf.write("\u018a\7\62\2\2\u0183\u0184\7\62\2\2\u0184\u0185\t\2\2")
        buf.write("\2\u0185\u018a\7\62\2\2\u0186\u0187\7\62\2\2\u0187\u0188")
        buf.write("\t\3\2\2\u0188\u018a\7\62\2\2\u0189\u0180\3\2\2\2\u0189")
        buf.write("\u0181\3\2\2\2\u0189\u0183\3\2\2\2\u0189\u0186\3\2\2\2")
        buf.write("\u018at\3\2\2\2\u018b\u0192\t\4\2\2\u018c\u018e\5k\66")
        buf.write("\2\u018d\u018c\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u0191\5\u0087D\2\u0190\u018d\3\2\2\2\u0191")
        buf.write("\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193v\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0197\5\u0087")
        buf.write("D\2\u0196\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199x\3\2\2\2\u019a\u019b")
        buf.write("\t\5\2\2\u019b\u01a2\t\6\2\2\u019c\u019e\5k\66\2\u019d")
        buf.write("\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f\u01a1\t\7\2\2\u01a0\u019d\3\2\2\2\u01a1\u01a4\3")
        buf.write("\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3z")
        buf.write("\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a6\t\5\2\2\u01a6")
        buf.write("\u01a7\t\3\2\2\u01a7\u01ae\t\b\2\2\u01a8\u01aa\5k\66\2")
        buf.write("\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\3")
        buf.write("\2\2\2\u01ab\u01ad\t\t\2\2\u01ac\u01a9\3\2\2\2\u01ad\u01b0")
        buf.write("\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af")
        buf.write("|\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\t\5\2\2\u01b2")
        buf.write("\u01b3\t\2\2\2\u01b3\u01ba\t\n\2\2\u01b4\u01b6\5k\66\2")
        buf.write("\u01b5\u01b4\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7\3")
        buf.write("\2\2\2\u01b7\u01b9\t\13\2\2\u01b8\u01b5\3\2\2\2\u01b9")
        buf.write("\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2")
        buf.write("\u01bb~\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01c0\5u;\2")
        buf.write("\u01be\u01c0\7\62\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01be")
        buf.write("\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c3\5\u0085C\2\u01c2")
        buf.write("\u01c4\5\u0083B\2\u01c3\u01c2\3\2\2\2\u01c3\u01c4\3\2")
        buf.write("\2\2\u01c4\u01ce\3\2\2\2\u01c5\u01c6\5\u0085C\2\u01c6")
        buf.write("\u01c7\5\u0083B\2\u01c7\u01ce\3\2\2\2\u01c8\u01cb\5u;")
        buf.write("\2\u01c9\u01cb\7\62\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ce\5\u0083B\2\u01cd")
        buf.write("\u01bf\3\2\2\2\u01cd\u01c5\3\2\2\2\u01cd\u01ca\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d0\b@\3\2\u01d0\u0080\3")
        buf.write("\2\2\2\u01d1\u01d5\t\f\2\2\u01d2\u01d4\5\u0093J\2\u01d3")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d5\u01d6\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7\u01d5\3")
        buf.write("\2\2\2\u01d8\u01d9\t\f\2\2\u01d9\u01da\3\2\2\2\u01da\u01db")
        buf.write("\bA\4\2\u01db\u0082\3\2\2\2\u01dc\u01de\t\r\2\2\u01dd")
        buf.write("\u01df\5\u0089E\2\u01de\u01dd\3\2\2\2\u01de\u01df\3\2")
        buf.write("\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\5w<\2\u01e1\u0084")
        buf.write("\3\2\2\2\u01e2\u01e4\5g\64\2\u01e3\u01e5\5w<\2\u01e4\u01e3")
        buf.write("\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u0086\3\2\2\2\u01e6")
        buf.write("\u01e7\t\16\2\2\u01e7\u0088\3\2\2\2\u01e8\u01e9\t\17\2")
        buf.write("\2\u01e9\u008a\3\2\2\2\u01ea\u01ee\t\20\2\2\u01eb\u01ed")
        buf.write("\t\21\2\2\u01ec\u01eb\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u008c\3\2\2\2")
        buf.write("\u01f0\u01ee\3\2\2\2\u01f1\u01f3\5\5\3\2\u01f2\u01f4\t")
        buf.write("\21\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5")
        buf.write("\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u008e\3\2\2\2")
        buf.write("\u01f7\u01f8\7%\2\2\u01f8\u01f9\7%\2\2\u01f9\u01fd\3\2")
        buf.write("\2\2\u01fa\u01fc\13\2\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff")
        buf.write("\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe")
        buf.write("\u0200\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0201\7%\2\2")
        buf.write("\u0201\u0202\7%\2\2\u0202\u0203\3\2\2\2\u0203\u0204\b")
        buf.write("H\5\2\u0204\u0090\3\2\2\2\u0205\u0207\t\22\2\2\u0206\u0205")
        buf.write("\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0206\3\2\2\2\u0208")
        buf.write("\u0209\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020b\bI\5\2")
        buf.write("\u020b\u0092\3\2\2\2\u020c\u0211\5\u0095K\2\u020d\u020e")
        buf.write("\t\23\2\2\u020e\u0211\t\f\2\2\u020f\u0211\n\24\2\2\u0210")
        buf.write("\u020c\3\2\2\2\u0210\u020d\3\2\2\2\u0210\u020f\3\2\2\2")
        buf.write("\u0211\u0094\3\2\2\2\u0212\u0213\7^\2\2\u0213\u0214\t")
        buf.write("\25\2\2\u0214\u0096\3\2\2\2\u0215\u0216\7^\2\2\u0216\u0217")
        buf.write("\n\25\2\2\u0217\u0098\3\2\2\2\u0218\u021c\t\f\2\2\u0219")
        buf.write("\u021b\5\u0093J\2\u021a\u0219\3\2\2\2\u021b\u021e\3\2")
        buf.write("\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u0220")
        buf.write("\3\2\2\2\u021e\u021c\3\2\2\2\u021f\u0221\t\26\2\2\u0220")
        buf.write("\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0223\bM\6\2")
        buf.write("\u0223\u009a\3\2\2\2\u0224\u0228\t\f\2\2\u0225\u0227\5")
        buf.write("\u0093J\2\u0226\u0225\3\2\2\2\u0227\u022a\3\2\2\2\u0228")
        buf.write("\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022b\3\2\2\2")
        buf.write("\u022a\u0228\3\2\2\2\u022b\u022c\5\u0097L\2\u022c\u022d")
        buf.write("\bN\7\2\u022d\u009c\3\2\2\2\u022e\u022f\13\2\2\2\u022f")
        buf.write("\u0230\bO\b\2\u0230\u009e\3\2\2\2\35\2\u017c\u0189\u018d")
        buf.write("\u0192\u0198\u019d\u01a2\u01a9\u01ae\u01b5\u01ba\u01bf")
        buf.write("\u01c3\u01ca\u01cd\u01d5\u01de\u01e4\u01ee\u01f5\u01fd")
        buf.write("\u0208\u0210\u021c\u0220\u0228\t\39\2\3@\3\3A\4\b\2\2")
        buf.write("\3M\5\3N\6\3O\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CLASS = 1
    SELF = 2
    BREAK = 3
    CONTINUE = 4
    RETURN = 5
    IF = 6
    ELSEIF = 7
    ELSE = 8
    FOREACH = 9
    IN = 10
    TRUE = 11
    FALSE = 12
    NULL = 13
    INT = 14
    FLOAT = 15
    BOOLEAN = 16
    STRING = 17
    ARRAY = 18
    CONSTRUCTOR = 19
    DESTRUCTOR = 20
    NEW = 21
    BY = 22
    VAR = 23
    VAL = 24
    NOT = 25
    AND = 26
    OR = 27
    EQSTR = 28
    CONCATSTR = 29
    ADD = 30
    SUB = 31
    MUL = 32
    DIV = 33
    MODULO = 34
    EQ = 35
    NEQ = 36
    LT = 37
    GT = 38
    LTE = 39
    GTE = 40
    ASSIGN = 41
    LP = 42
    RP = 43
    LB = 44
    RB = 45
    SEMI = 46
    COLON = 47
    COMMA = 48
    DOTDOT = 49
    DOT = 50
    DOUBLECOLON = 51
    LSB = 52
    RSB = 53
    INTEGER_LITERAL = 54
    ZERO_INTLIT = 55
    FLOAT_LITERAL = 56
    STRING_LITERAL = 57
    ID = 58
    DOLLARID = 59
    COMMENT = 60
    WS = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Class'", "'Self'", "'Break'", "'Continue'", "'Return'", "'If'", 
            "'Elseif'", "'Else'", "'Foreach'", "'In'", "'True'", "'False'", 
            "'Null'", "'Int'", "'Float'", "'Boolean'", "'String'", "'Array'", 
            "'Constructor'", "'Destructor'", "'New'", "'By'", "'Var'", "'Val'", 
            "'!'", "'&&'", "'||'", "'==.'", "'+.'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'='", "'('", "')'", "'{'", "'}'", "';'", "':'", "','", "'..'", 
            "'.'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "CLASS", "SELF", "BREAK", "CONTINUE", "RETURN", "IF", "ELSEIF", 
            "ELSE", "FOREACH", "IN", "TRUE", "FALSE", "NULL", "INT", "FLOAT", 
            "BOOLEAN", "STRING", "ARRAY", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
            "BY", "VAR", "VAL", "NOT", "AND", "OR", "EQSTR", "CONCATSTR", 
            "ADD", "SUB", "MUL", "DIV", "MODULO", "EQ", "NEQ", "LT", "GT", 
            "LTE", "GTE", "ASSIGN", "LP", "RP", "LB", "RB", "SEMI", "COLON", 
            "COMMA", "DOTDOT", "DOT", "DOUBLECOLON", "LSB", "RSB", "INTEGER_LITERAL", 
            "ZERO_INTLIT", "FLOAT_LITERAL", "STRING_LITERAL", "ID", "DOLLARID", 
            "COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "CLASS", "STATIC", "SELF", "BREAK", "CONTINUE", "RETURN", 
                  "IF", "ELSEIF", "ELSE", "FOREACH", "IN", "TRUE", "FALSE", 
                  "NULL", "INT", "FLOAT", "BOOLEAN", "STRING", "ARRAY", 
                  "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "VAR", "VAL", 
                  "NOT", "AND", "OR", "EQSTR", "CONCATSTR", "ADD", "SUB", 
                  "MUL", "DIV", "MODULO", "EQ", "NEQ", "LT", "GT", "LTE", 
                  "GTE", "ASSIGN", "LP", "RP", "LB", "RB", "SEMI", "COLON", 
                  "COMMA", "DOTDOT", "DOT", "DOUBLECOLON", "UNDERLINE", 
                  "LSB", "RSB", "INTEGER_LITERAL", "ZERO_INTLIT", "DEC", 
                  "Decwithzero", "OCT", "HEX", "BIN", "FLOAT_LITERAL", "STRING_LITERAL", 
                  "EXPONENTIAL", "DEC_PART", "DIGIT", "SIGN", "ID", "DOLLARID", 
                  "COMMENT", "WS", "STRCHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[55] = self.INTEGER_LITERAL_action 
            actions[62] = self.FLOAT_LITERAL_action 
            actions[63] = self.STRING_LITERAL_action 
            actions[75] = self.UNCLOSE_STRING_action 
            actions[76] = self.ILLEGAL_ESCAPE_action 
            actions[77] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                                    self.text = self.text.replace('_', '')
                                
     

    def FLOAT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                                    self.text = self.text.replace('_', '')
                                
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                                    self.text = self.text[1:-1]
                                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                                    y = str(self.text)
                                    if y[-1] == '\n':
                                        raise UncloseString(y[1:-2])
                                    else:
                                        raise UncloseString(y[1:])
                                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                                    y = str(self.text)
                                    raise IllegalEscape(y[1:])
                                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                        raise ErrorToken(self.text)
                    
     


