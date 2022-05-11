# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u0220\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\3\2\6\2n\n\2\r\2\16\2o\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3x\n\3\3\3\3\3\7\3|\n\3\f\3\16\3\177")
        buf.write("\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0089\n\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\7\5\u0090\n\5\f\5\16\5\u0093\13\5\3")
        buf.write("\6\3\6\3\7\3\7\3\7\5\7\u009a\n\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\5\7\u00a3\n\7\3\b\3\b\3\b\5\b\u00a8\n\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\5\n\u00b8")
        buf.write("\n\n\3\13\7\13\u00bb\n\13\f\13\16\13\u00be\13\13\3\f\7")
        buf.write("\f\u00c1\n\f\f\f\16\f\u00c4\13\f\3\r\3\r\3\r\7\r\u00c9")
        buf.write("\n\r\f\r\16\r\u00cc\13\r\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\7\17\u00d5\n\17\f\17\16\17\u00d8\13\17\3\20\3\20")
        buf.write("\3\20\5\20\u00dd\n\20\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00f1\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\5\24\u00fc\n\24\3\25\3\25\3\25\3\25\7\25")
        buf.write("\u0102\n\25\f\25\16\25\u0105\13\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u010b\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u0120\n\27\3\30\3\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\7\31\u012a\n\31\f\31\16\31\u012d\13\31\3\31\5")
        buf.write("\31\u0130\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0144\n\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3")
        buf.write("\36\3\37\3\37\5\37\u0151\n\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \5 \u015f\n \3!\3!\7!\u0163\n!\f!\16!")
        buf.write("\u0166\13!\3!\3!\3\"\3\"\3#\3#\3#\3#\3#\5#\u0171\n#\3")
        buf.write("$\3$\3$\3$\3$\5$\u0178\n$\3%\3%\3%\3%\3%\3%\7%\u0180\n")
        buf.write("%\f%\16%\u0183\13%\3&\3&\3&\3&\3&\3&\7&\u018b\n&\f&\16")
        buf.write("&\u018e\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0196\n\'\f\'")
        buf.write("\16\'\u0199\13\'\3(\3(\3(\5(\u019e\n(\3)\3)\3)\5)\u01a3")
        buf.write("\n)\3*\3*\3*\3*\3*\7*\u01aa\n*\f*\16*\u01ad\13*\3+\3+")
        buf.write("\3+\3+\3+\3+\7+\u01b5\n+\f+\16+\u01b8\13+\3,\3,\3,\3,")
        buf.write("\3,\3,\7,\u01c0\n,\f,\16,\u01c3\13,\3-\3-\3-\5-\u01c8")
        buf.write("\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01d4\n.\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\5/\u01df\n/\3\60\3\60\3\60\5\60\u01e4")
        buf.write("\n\60\3\60\3\60\3\61\3\61\3\61\5\61\u01eb\n\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\5\62\u01f2\n\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\7\63\u01f9\n\63\f\63\16\63\u01fc\13\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0208\n")
        buf.write("\64\3\65\3\65\3\66\3\66\3\66\3\66\3\66\7\66\u0211\n\66")
        buf.write("\f\66\16\66\u0214\13\66\3\66\3\66\3\66\3\66\3\66\5\66")
        buf.write("\u021b\n\66\3\66\5\66\u021e\n\66\3\66\2\bHJLRTV\67\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhj\2\13\3\2\31\32\3\2<=\3")
        buf.write("\2\20\23\3\2%*\3\2\36\37\3\2\34\35\3\2 !\3\2\"$\3\2\r")
        buf.write("\16\2\u0236\2m\3\2\2\2\4s\3\2\2\2\6\u0082\3\2\2\2\b\u008c")
        buf.write("\3\2\2\2\n\u0094\3\2\2\2\f\u00a2\3\2\2\2\16\u00a4\3\2")
        buf.write("\2\2\20\u00ae\3\2\2\2\22\u00b7\3\2\2\2\24\u00bc\3\2\2")
        buf.write("\2\26\u00c2\3\2\2\2\30\u00c5\3\2\2\2\32\u00cd\3\2\2\2")
        buf.write("\34\u00d1\3\2\2\2\36\u00dc\3\2\2\2 \u00de\3\2\2\2\"\u00e0")
        buf.write("\3\2\2\2$\u00f0\3\2\2\2&\u00fb\3\2\2\2(\u00fd\3\2\2\2")
        buf.write("*\u010e\3\2\2\2,\u011f\3\2\2\2.\u0121\3\2\2\2\60\u0123")
        buf.write("\3\2\2\2\62\u0131\3\2\2\2\64\u0137\3\2\2\2\66\u013a\3")
        buf.write("\2\2\28\u0148\3\2\2\2:\u014b\3\2\2\2<\u014e\3\2\2\2>\u015e")
        buf.write("\3\2\2\2@\u0160\3\2\2\2B\u0169\3\2\2\2D\u0170\3\2\2\2")
        buf.write("F\u0177\3\2\2\2H\u0179\3\2\2\2J\u0184\3\2\2\2L\u018f\3")
        buf.write("\2\2\2N\u019d\3\2\2\2P\u01a2\3\2\2\2R\u01a4\3\2\2\2T\u01ae")
        buf.write("\3\2\2\2V\u01b9\3\2\2\2X\u01c7\3\2\2\2Z\u01d3\3\2\2\2")
        buf.write("\\\u01de\3\2\2\2^\u01e0\3\2\2\2`\u01e7\3\2\2\2b\u01ee")
        buf.write("\3\2\2\2d\u01fa\3\2\2\2f\u0207\3\2\2\2h\u0209\3\2\2\2")
        buf.write("j\u021d\3\2\2\2ln\5\4\3\2ml\3\2\2\2no\3\2\2\2om\3\2\2")
        buf.write("\2op\3\2\2\2pq\3\2\2\2qr\7\2\2\3r\3\3\2\2\2st\7\3\2\2")
        buf.write("tw\7<\2\2uv\7\61\2\2vx\7<\2\2wu\3\2\2\2wx\3\2\2\2xy\3")
        buf.write("\2\2\2y}\7.\2\2z|\5\22\n\2{z\3\2\2\2|\177\3\2\2\2}{\3")
        buf.write("\2\2\2}~\3\2\2\2~\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0081")
        buf.write("\7/\2\2\u0081\5\3\2\2\2\u0082\u0083\t\2\2\2\u0083\u0084")
        buf.write("\5\b\5\2\u0084\u0085\7\61\2\2\u0085\u0088\5\36\20\2\u0086")
        buf.write("\u0087\7+\2\2\u0087\u0089\5d\63\2\u0088\u0086\3\2\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\7")
        buf.write("\60\2\2\u008b\7\3\2\2\2\u008c\u0091\5\n\6\2\u008d\u008e")
        buf.write("\7\62\2\2\u008e\u0090\5\n\6\2\u008f\u008d\3\2\2\2\u0090")
        buf.write("\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\t\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\t\3\2")
        buf.write("\2\u0095\13\3\2\2\2\u0096\u0097\5\n\6\2\u0097\u0099\7")
        buf.write(",\2\2\u0098\u009a\5\30\r\2\u0099\u0098\3\2\2\2\u0099\u009a")
        buf.write("\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\7-\2\2\u009c")
        buf.write("\u009d\7.\2\2\u009d\u009e\5\24\13\2\u009e\u009f\7/\2\2")
        buf.write("\u009f\u00a3\3\2\2\2\u00a0\u00a3\5\16\b\2\u00a1\u00a3")
        buf.write("\5\20\t\2\u00a2\u0096\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2")
        buf.write("\u00a1\3\2\2\2\u00a3\r\3\2\2\2\u00a4\u00a5\7\25\2\2\u00a5")
        buf.write("\u00a7\7,\2\2\u00a6\u00a8\5\30\r\2\u00a7\u00a6\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\7")
        buf.write("-\2\2\u00aa\u00ab\7.\2\2\u00ab\u00ac\5\26\f\2\u00ac\u00ad")
        buf.write("\7/\2\2\u00ad\17\3\2\2\2\u00ae\u00af\7\26\2\2\u00af\u00b0")
        buf.write("\7,\2\2\u00b0\u00b1\7-\2\2\u00b1\u00b2\7.\2\2\u00b2\u00b3")
        buf.write("\5\26\f\2\u00b3\u00b4\7/\2\2\u00b4\21\3\2\2\2\u00b5\u00b8")
        buf.write("\5\6\4\2\u00b6\u00b8\5\f\7\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b8\23\3\2\2\2\u00b9\u00bb\5&\24\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bd\25\3\2\2\2\u00be\u00bc\3\2")
        buf.write("\2\2\u00bf\u00c1\5$\23\2\u00c0\u00bf\3\2\2\2\u00c1\u00c4")
        buf.write("\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\27\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00ca\5\32\16\2")
        buf.write("\u00c6\u00c7\7\60\2\2\u00c7\u00c9\5\32\16\2\u00c8\u00c6")
        buf.write("\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\31\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd")
        buf.write("\u00ce\5\34\17\2\u00ce\u00cf\7\61\2\2\u00cf\u00d0\5\36")
        buf.write("\20\2\u00d0\33\3\2\2\2\u00d1\u00d6\7<\2\2\u00d2\u00d3")
        buf.write("\7\62\2\2\u00d3\u00d5\7<\2\2\u00d4\u00d2\3\2\2\2\u00d5")
        buf.write("\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2")
        buf.write("\u00d7\35\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00dd\5 \21")
        buf.write("\2\u00da\u00dd\5\"\22\2\u00db\u00dd\7<\2\2\u00dc\u00d9")
        buf.write("\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd")
        buf.write("\37\3\2\2\2\u00de\u00df\t\4\2\2\u00df!\3\2\2\2\u00e0\u00e1")
        buf.write("\7\24\2\2\u00e1\u00e2\7\66\2\2\u00e2\u00e3\5\36\20\2\u00e3")
        buf.write("\u00e4\7\62\2\2\u00e4\u00e5\78\2\2\u00e5\u00e6\7\67\2")
        buf.write("\2\u00e6#\3\2\2\2\u00e7\u00f1\5(\25\2\u00e8\u00f1\5*\26")
        buf.write("\2\u00e9\u00f1\5\60\31\2\u00ea\u00f1\5\66\34\2\u00eb\u00f1")
        buf.write("\58\35\2\u00ec\u00f1\5:\36\2\u00ed\u00f1\5<\37\2\u00ee")
        buf.write("\u00f1\5> \2\u00ef\u00f1\5@!\2\u00f0\u00e7\3\2\2\2\u00f0")
        buf.write("\u00e8\3\2\2\2\u00f0\u00e9\3\2\2\2\u00f0\u00ea\3\2\2\2")
        buf.write("\u00f0\u00eb\3\2\2\2\u00f0\u00ec\3\2\2\2\u00f0\u00ed\3")
        buf.write("\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1%")
        buf.write("\3\2\2\2\u00f2\u00fc\5(\25\2\u00f3\u00fc\5*\26\2\u00f4")
        buf.write("\u00fc\5\60\31\2\u00f5\u00fc\5\66\34\2\u00f6\u00fc\58")
        buf.write("\35\2\u00f7\u00fc\5:\36\2\u00f8\u00fc\5<\37\2\u00f9\u00fc")
        buf.write("\5> \2\u00fa\u00fc\5@!\2\u00fb\u00f2\3\2\2\2\u00fb\u00f3")
        buf.write("\3\2\2\2\u00fb\u00f4\3\2\2\2\u00fb\u00f5\3\2\2\2\u00fb")
        buf.write("\u00f6\3\2\2\2\u00fb\u00f7\3\2\2\2\u00fb\u00f8\3\2\2\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\'\3\2\2")
        buf.write("\2\u00fd\u00fe\t\2\2\2\u00fe\u0103\7<\2\2\u00ff\u0100")
        buf.write("\7\62\2\2\u0100\u0102\7<\2\2\u0101\u00ff\3\2\2\2\u0102")
        buf.write("\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0104\u0106\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0107\7")
        buf.write("\61\2\2\u0107\u010a\5\36\20\2\u0108\u0109\7+\2\2\u0109")
        buf.write("\u010b\5d\63\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b\u010c\3\2\2\2\u010c\u010d\7\60\2\2\u010d)\3\2\2")
        buf.write("\2\u010e\u010f\5,\27\2\u010f\u0110\7+\2\2\u0110\u0111")
        buf.write("\5.\30\2\u0111\u0112\7\60\2\2\u0112+\3\2\2\2\u0113\u0120")
        buf.write("\t\3\2\2\u0114\u0115\5Z.\2\u0115\u0116\5\\/\2\u0116\u0120")
        buf.write("\3\2\2\2\u0117\u0118\5D#\2\u0118\u0119\7\64\2\2\u0119")
        buf.write("\u011a\7<\2\2\u011a\u0120\3\2\2\2\u011b\u011c\7<\2\2\u011c")
        buf.write("\u011d\7\65\2\2\u011d\u0120\7=\2\2\u011e\u0120\5D#\2\u011f")
        buf.write("\u0113\3\2\2\2\u011f\u0114\3\2\2\2\u011f\u0117\3\2\2\2")
        buf.write("\u011f\u011b\3\2\2\2\u011f\u011e\3\2\2\2\u0120-\3\2\2")
        buf.write("\2\u0121\u0122\5D#\2\u0122/\3\2\2\2\u0123\u0124\7\b\2")
        buf.write("\2\u0124\u0125\7,\2\2\u0125\u0126\5D#\2\u0126\u0127\7")
        buf.write("-\2\2\u0127\u012b\5@!\2\u0128\u012a\5\62\32\2\u0129\u0128")
        buf.write("\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129\3\2\2\2\u012b")
        buf.write("\u012c\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012e\u0130\5\64\33\2\u012f\u012e\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130\61\3\2\2\2\u0131\u0132\7\t\2\2\u0132\u0133")
        buf.write("\7,\2\2\u0133\u0134\5D#\2\u0134\u0135\7-\2\2\u0135\u0136")
        buf.write("\5@!\2\u0136\63\3\2\2\2\u0137\u0138\7\n\2\2\u0138\u0139")
        buf.write("\5@!\2\u0139\65\3\2\2\2\u013a\u013b\7\13\2\2\u013b\u013c")
        buf.write("\7,\2\2\u013c\u013d\t\3\2\2\u013d\u013e\7\f\2\2\u013e")
        buf.write("\u013f\5D#\2\u013f\u0140\7\63\2\2\u0140\u0143\5D#\2\u0141")
        buf.write("\u0142\7\30\2\2\u0142\u0144\5D#\2\u0143\u0141\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\7")
        buf.write("-\2\2\u0146\u0147\5@!\2\u0147\67\3\2\2\2\u0148\u0149\7")
        buf.write("\5\2\2\u0149\u014a\7\60\2\2\u014a9\3\2\2\2\u014b\u014c")
        buf.write("\7\6\2\2\u014c\u014d\7\60\2\2\u014d;\3\2\2\2\u014e\u0150")
        buf.write("\7\7\2\2\u014f\u0151\5D#\2\u0150\u014f\3\2\2\2\u0150\u0151")
        buf.write("\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153\7\60\2\2\u0153")
        buf.write("=\3\2\2\2\u0154\u0155\5D#\2\u0155\u0156\7\64\2\2\u0156")
        buf.write("\u0157\5^\60\2\u0157\u0158\7\60\2\2\u0158\u015f\3\2\2")
        buf.write("\2\u0159\u015a\7<\2\2\u015a\u015b\7\65\2\2\u015b\u015c")
        buf.write("\5`\61\2\u015c\u015d\7\60\2\2\u015d\u015f\3\2\2\2\u015e")
        buf.write("\u0154\3\2\2\2\u015e\u0159\3\2\2\2\u015f?\3\2\2\2\u0160")
        buf.write("\u0164\7.\2\2\u0161\u0163\5&\24\2\u0162\u0161\3\2\2\2")
        buf.write("\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u0167\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168")
        buf.write("\7/\2\2\u0168A\3\2\2\2\u0169\u016a\t\5\2\2\u016aC\3\2")
        buf.write("\2\2\u016b\u016c\5F$\2\u016c\u016d\t\6\2\2\u016d\u016e")
        buf.write("\5F$\2\u016e\u0171\3\2\2\2\u016f\u0171\5F$\2\u0170\u016b")
        buf.write("\3\2\2\2\u0170\u016f\3\2\2\2\u0171E\3\2\2\2\u0172\u0173")
        buf.write("\5H%\2\u0173\u0174\5B\"\2\u0174\u0175\5H%\2\u0175\u0178")
        buf.write("\3\2\2\2\u0176\u0178\5H%\2\u0177\u0172\3\2\2\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178G\3\2\2\2\u0179\u017a\b%\1\2\u017a\u017b")
        buf.write("\5J&\2\u017b\u0181\3\2\2\2\u017c\u017d\f\4\2\2\u017d\u017e")
        buf.write("\t\7\2\2\u017e\u0180\5J&\2\u017f\u017c\3\2\2\2\u0180\u0183")
        buf.write("\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("I\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\b&\1\2\u0185")
        buf.write("\u0186\5L\'\2\u0186\u018c\3\2\2\2\u0187\u0188\f\4\2\2")
        buf.write("\u0188\u0189\t\b\2\2\u0189\u018b\5L\'\2\u018a\u0187\3")
        buf.write("\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018dK\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190")
        buf.write("\b\'\1\2\u0190\u0191\5N(\2\u0191\u0197\3\2\2\2\u0192\u0193")
        buf.write("\f\4\2\2\u0193\u0194\t\t\2\2\u0194\u0196\5N(\2\u0195\u0192")
        buf.write("\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198M\3\2\2\2\u0199\u0197\3\2\2\2\u019a")
        buf.write("\u019b\7\33\2\2\u019b\u019e\5N(\2\u019c\u019e\5P)\2\u019d")
        buf.write("\u019a\3\2\2\2\u019d\u019c\3\2\2\2\u019eO\3\2\2\2\u019f")
        buf.write("\u01a0\7!\2\2\u01a0\u01a3\5P)\2\u01a1\u01a3\5R*\2\u01a2")
        buf.write("\u019f\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3Q\3\2\2\2\u01a4")
        buf.write("\u01a5\b*\1\2\u01a5\u01a6\5T+\2\u01a6\u01ab\3\2\2\2\u01a7")
        buf.write("\u01a8\f\4\2\2\u01a8\u01aa\5\\/\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01acS\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01af")
        buf.write("\b+\1\2\u01af\u01b0\5V,\2\u01b0\u01b6\3\2\2\2\u01b1\u01b2")
        buf.write("\f\4\2\2\u01b2\u01b3\7\64\2\2\u01b3\u01b5\5V,\2\u01b4")
        buf.write("\u01b1\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7U\3\2\2\2\u01b8\u01b6\3\2\2")
        buf.write("\2\u01b9\u01ba\b,\1\2\u01ba\u01bb\5X-\2\u01bb\u01c1\3")
        buf.write("\2\2\2\u01bc\u01bd\f\4\2\2\u01bd\u01be\7\65\2\2\u01be")
        buf.write("\u01c0\5X-\2\u01bf\u01bc\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1")
        buf.write("\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2W\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c4\u01c5\7\27\2\2\u01c5\u01c8\5X-\2")
        buf.write("\u01c6\u01c8\5Z.\2\u01c7\u01c4\3\2\2\2\u01c7\u01c6\3\2")
        buf.write("\2\2\u01c8Y\3\2\2\2\u01c9\u01d4\5f\64\2\u01ca\u01d4\5")
        buf.write("^\60\2\u01cb\u01d4\5`\61\2\u01cc\u01d4\5\\/\2\u01cd\u01d4")
        buf.write("\5b\62\2\u01ce\u01cf\7,\2\2\u01cf\u01d0\5D#\2\u01d0\u01d1")
        buf.write("\7-\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d4\t\3\2\2\u01d3")
        buf.write("\u01c9\3\2\2\2\u01d3\u01ca\3\2\2\2\u01d3\u01cb\3\2\2\2")
        buf.write("\u01d3\u01cc\3\2\2\2\u01d3\u01cd\3\2\2\2\u01d3\u01ce\3")
        buf.write("\2\2\2\u01d3\u01d2\3\2\2\2\u01d4[\3\2\2\2\u01d5\u01d6")
        buf.write("\7\66\2\2\u01d6\u01d7\5D#\2\u01d7\u01d8\7\67\2\2\u01d8")
        buf.write("\u01d9\5\\/\2\u01d9\u01df\3\2\2\2\u01da\u01db\7\66\2\2")
        buf.write("\u01db\u01dc\5D#\2\u01dc\u01dd\7\67\2\2\u01dd\u01df\3")
        buf.write("\2\2\2\u01de\u01d5\3\2\2\2\u01de\u01da\3\2\2\2\u01df]")
        buf.write("\3\2\2\2\u01e0\u01e1\7<\2\2\u01e1\u01e3\7,\2\2\u01e2\u01e4")
        buf.write("\5d\63\2\u01e3\u01e2\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write("\u01e5\3\2\2\2\u01e5\u01e6\7-\2\2\u01e6_\3\2\2\2\u01e7")
        buf.write("\u01e8\7=\2\2\u01e8\u01ea\7,\2\2\u01e9\u01eb\5d\63\2\u01ea")
        buf.write("\u01e9\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\3\2\2\2")
        buf.write("\u01ec\u01ed\7-\2\2\u01eda\3\2\2\2\u01ee\u01ef\7<\2\2")
        buf.write("\u01ef\u01f1\7,\2\2\u01f0\u01f2\5d\63\2\u01f1\u01f0\3")
        buf.write("\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4")
        buf.write("\7-\2\2\u01f4c\3\2\2\2\u01f5\u01f6\5D#\2\u01f6\u01f7\7")
        buf.write("\62\2\2\u01f7\u01f9\3\2\2\2\u01f8\u01f5\3\2\2\2\u01f9")
        buf.write("\u01fc\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2")
        buf.write("\u01fb\u01fd\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd\u01fe\5")
        buf.write("D#\2\u01fee\3\2\2\2\u01ff\u0208\78\2\2\u0200\u0208\79")
        buf.write("\2\2\u0201\u0208\7:\2\2\u0202\u0208\7;\2\2\u0203\u0208")
        buf.write("\5j\66\2\u0204\u0208\5h\65\2\u0205\u0208\7\4\2\2\u0206")
        buf.write("\u0208\7\17\2\2\u0207\u01ff\3\2\2\2\u0207\u0200\3\2\2")
        buf.write("\2\u0207\u0201\3\2\2\2\u0207\u0202\3\2\2\2\u0207\u0203")
        buf.write("\3\2\2\2\u0207\u0204\3\2\2\2\u0207\u0205\3\2\2\2\u0207")
        buf.write("\u0206\3\2\2\2\u0208g\3\2\2\2\u0209\u020a\t\n\2\2\u020a")
        buf.write("i\3\2\2\2\u020b\u020c\7\24\2\2\u020c\u020d\7,\2\2\u020d")
        buf.write("\u0212\5j\66\2\u020e\u020f\7\62\2\2\u020f\u0211\5j\66")
        buf.write("\2\u0210\u020e\3\2\2\2\u0211\u0214\3\2\2\2\u0212\u0210")
        buf.write("\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0215\3\2\2\2\u0214")
        buf.write("\u0212\3\2\2\2\u0215\u0216\7-\2\2\u0216\u021e\3\2\2\2")
        buf.write("\u0217\u0218\7\24\2\2\u0218\u021a\7,\2\2\u0219\u021b\5")
        buf.write("d\63\2\u021a\u0219\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021c")
        buf.write("\3\2\2\2\u021c\u021e\7-\2\2\u021d\u020b\3\2\2\2\u021d")
        buf.write("\u0217\3\2\2\2\u021ek\3\2\2\2\60ow}\u0088\u0091\u0099")
        buf.write("\u00a2\u00a7\u00b7\u00bc\u00c2\u00ca\u00d6\u00dc\u00f0")
        buf.write("\u00fb\u0103\u010a\u011f\u012b\u012f\u0143\u0150\u015e")
        buf.write("\u0164\u0170\u0177\u0181\u018c\u0197\u019d\u01a2\u01ab")
        buf.write("\u01b6\u01c1\u01c7\u01d3\u01de\u01e3\u01ea\u01f1\u01fa")
        buf.write("\u0207\u0212\u021a\u021d")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Class'", "'Self'", "'Break'", "'Continue'", 
                     "'Return'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
                     "'In'", "'True'", "'False'", "'Null'", "'Int'", "'Float'", 
                     "'Boolean'", "'String'", "'Array'", "'Constructor'", 
                     "'Destructor'", "'New'", "'By'", "'Var'", "'Val'", 
                     "'!'", "'&&'", "'||'", "'==.'", "'+.'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'='", "'('", "')'", "'{'", "'}'", 
                     "';'", "':'", "','", "'..'", "'.'", "<INVALID>", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "SELF", "BREAK", "CONTINUE", 
                      "RETURN", "IF", "ELSEIF", "ELSE", "FOREACH", "IN", 
                      "TRUE", "FALSE", "NULL", "INT", "FLOAT", "BOOLEAN", 
                      "STRING", "ARRAY", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                      "BY", "VAR", "VAL", "NOT", "AND", "OR", "EQSTR", "CONCATSTR", 
                      "ADD", "SUB", "MUL", "DIV", "MODULO", "EQ", "NEQ", 
                      "LT", "GT", "LTE", "GTE", "ASSIGN", "LP", "RP", "LB", 
                      "RB", "SEMI", "COLON", "COMMA", "DOTDOT", "DOT", "DOUBLECOLON", 
                      "LSB", "RSB", "INTEGER_LITERAL", "ZERO_INTLIT", "FLOAT_LITERAL", 
                      "STRING_LITERAL", "ID", "DOLLARID", "COMMENT", "WS", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declare = 1
    RULE_att_declare = 2
    RULE_mixed_list = 3
    RULE_member_id = 4
    RULE_method_declare = 5
    RULE_constructor_declare = 6
    RULE_destructor_declare = 7
    RULE_class_body = 8
    RULE_body = 9
    RULE_cons_des_body = 10
    RULE_param_list = 11
    RULE_id_list_with_type = 12
    RULE_ids_list = 13
    RULE_type_name = 14
    RULE_primitive_type = 15
    RULE_arr_type = 16
    RULE_cons_des_stmt = 17
    RULE_stmt = 18
    RULE_var_declare = 19
    RULE_assignment = 20
    RULE_assign_lhs = 21
    RULE_assign_rhs = 22
    RULE_if_stmt = 23
    RULE_elseif_stmt = 24
    RULE_else_stmt = 25
    RULE_for_stmt = 26
    RULE_break_stmt = 27
    RULE_continue_stmt = 28
    RULE_return_stmt = 29
    RULE_method_invoc_stmt = 30
    RULE_block_stmt = 31
    RULE_relational = 32
    RULE_exp = 33
    RULE_exp1 = 34
    RULE_exp2 = 35
    RULE_exp3 = 36
    RULE_exp4 = 37
    RULE_exp5 = 38
    RULE_exp6 = 39
    RULE_exp7 = 40
    RULE_exp8 = 41
    RULE_exp9 = 42
    RULE_exp10 = 43
    RULE_operands = 44
    RULE_index = 45
    RULE_instance_method = 46
    RULE_static_method = 47
    RULE_obj_create = 48
    RULE_exp_list = 49
    RULE_literal = 50
    RULE_boolean_literal = 51
    RULE_array_literal = 52

    ruleNames =  [ "program", "class_declare", "att_declare", "mixed_list", 
                   "member_id", "method_declare", "constructor_declare", 
                   "destructor_declare", "class_body", "body", "cons_des_body", 
                   "param_list", "id_list_with_type", "ids_list", "type_name", 
                   "primitive_type", "arr_type", "cons_des_stmt", "stmt", 
                   "var_declare", "assignment", "assign_lhs", "assign_rhs", 
                   "if_stmt", "elseif_stmt", "else_stmt", "for_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "method_invoc_stmt", 
                   "block_stmt", "relational", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", "exp10", 
                   "operands", "index", "instance_method", "static_method", 
                   "obj_create", "exp_list", "literal", "boolean_literal", 
                   "array_literal" ]

    EOF = Token.EOF
    CLASS=1
    SELF=2
    BREAK=3
    CONTINUE=4
    RETURN=5
    IF=6
    ELSEIF=7
    ELSE=8
    FOREACH=9
    IN=10
    TRUE=11
    FALSE=12
    NULL=13
    INT=14
    FLOAT=15
    BOOLEAN=16
    STRING=17
    ARRAY=18
    CONSTRUCTOR=19
    DESTRUCTOR=20
    NEW=21
    BY=22
    VAR=23
    VAL=24
    NOT=25
    AND=26
    OR=27
    EQSTR=28
    CONCATSTR=29
    ADD=30
    SUB=31
    MUL=32
    DIV=33
    MODULO=34
    EQ=35
    NEQ=36
    LT=37
    GT=38
    LTE=39
    GTE=40
    ASSIGN=41
    LP=42
    RP=43
    LB=44
    RB=45
    SEMI=46
    COLON=47
    COMMA=48
    DOTDOT=49
    DOT=50
    DOUBLECOLON=51
    LSB=52
    RSB=53
    INTEGER_LITERAL=54
    ZERO_INTLIT=55
    FLOAT_LITERAL=56
    STRING_LITERAL=57
    ID=58
    DOLLARID=59
    COMMENT=60
    WS=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    ERROR_CHAR=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declareContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declareContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.class_declare()
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 111
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def class_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_bodyContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_bodyContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declare" ):
                return visitor.visitClass_declare(self)
            else:
                return visitor.visitChildren(self)




    def class_declare(self):

        localctx = D96Parser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(D96Parser.CLASS)

            self.state = 114
            self.match(D96Parser.ID)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 115
                self.match(D96Parser.COLON)

                self.state = 116
                self.match(D96Parser.ID)


            self.state = 119
            self.match(D96Parser.LB)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLARID))) != 0):
                self.state = 120
                self.class_body()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Att_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mixed_list(self):
            return self.getTypedRuleContext(D96Parser.Mixed_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_att_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_declare" ):
                return visitor.visitAtt_declare(self)
            else:
                return visitor.visitChildren(self)




    def att_declare(self):

        localctx = D96Parser.Att_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_att_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 129
            self.mixed_list()
            self.state = 130
            self.match(D96Parser.COLON)
            self.state = 131
            self.type_name()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 132
                self.match(D96Parser.ASSIGN)
                self.state = 133
                self.exp_list()


            self.state = 136
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mixed_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Member_idContext)
            else:
                return self.getTypedRuleContext(D96Parser.Member_idContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_mixed_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMixed_list" ):
                return visitor.visitMixed_list(self)
            else:
                return visitor.visitChildren(self)




    def mixed_list(self):

        localctx = D96Parser.Mixed_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mixed_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.member_id()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 139
                self.match(D96Parser.COMMA)
                self.state = 140
                self.member_id()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_member_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_id" ):
                return visitor.visitMember_id(self)
            else:
                return visitor.visitChildren(self)




    def member_id(self):

        localctx = D96Parser.Member_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLARID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_id(self):
            return self.getTypedRuleContext(D96Parser.Member_idContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def body(self):
            return self.getTypedRuleContext(D96Parser.BodyContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def param_list(self):
            return self.getTypedRuleContext(D96Parser.Param_listContext,0)


        def constructor_declare(self):
            return self.getTypedRuleContext(D96Parser.Constructor_declareContext,0)


        def destructor_declare(self):
            return self.getTypedRuleContext(D96Parser.Destructor_declareContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declare" ):
                return visitor.visitMethod_declare(self)
            else:
                return visitor.visitChildren(self)




    def method_declare(self):

        localctx = D96Parser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.member_id()
                self.state = 149
                self.match(D96Parser.LP)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ID:
                    self.state = 150
                    self.param_list()


                self.state = 153
                self.match(D96Parser.RP)
                self.state = 154
                self.match(D96Parser.LB)
                self.state = 155
                self.body()
                self.state = 156
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.constructor_declare()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.destructor_declare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def cons_des_body(self):
            return self.getTypedRuleContext(D96Parser.Cons_des_bodyContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def param_list(self):
            return self.getTypedRuleContext(D96Parser.Param_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_declare" ):
                return visitor.visitConstructor_declare(self)
            else:
                return visitor.visitChildren(self)




    def constructor_declare(self):

        localctx = D96Parser.Constructor_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constructor_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 163
            self.match(D96Parser.LP)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 164
                self.param_list()


            self.state = 167
            self.match(D96Parser.RP)
            self.state = 168
            self.match(D96Parser.LB)
            self.state = 169
            self.cons_des_body()
            self.state = 170
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def cons_des_body(self):
            return self.getTypedRuleContext(D96Parser.Cons_des_bodyContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_destructor_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor_declare" ):
                return visitor.visitDestructor_declare(self)
            else:
                return visitor.visitChildren(self)




    def destructor_declare(self):

        localctx = D96Parser.Destructor_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_destructor_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(D96Parser.DESTRUCTOR)
            self.state = 173
            self.match(D96Parser.LP)
            self.state = 174
            self.match(D96Parser.RP)
            self.state = 175
            self.match(D96Parser.LB)
            self.state = 176
            self.cons_des_body()
            self.state = 177
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def att_declare(self):
            return self.getTypedRuleContext(D96Parser.Att_declareContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(D96Parser.Method_declareContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_class_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR, D96Parser.VAL]:
                self.state = 179
                self.att_declare()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLARID]:
                self.state = 180
                self.method_declare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.RETURN) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.LP) | (1 << D96Parser.LB) | (1 << D96Parser.LSB) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.ZERO_INTLIT) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLARID))) != 0):
                self.state = 183
                self.stmt()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cons_des_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cons_des_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Cons_des_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Cons_des_stmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_cons_des_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCons_des_body" ):
                return visitor.visitCons_des_body(self)
            else:
                return visitor.visitChildren(self)




    def cons_des_body(self):

        localctx = D96Parser.Cons_des_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cons_des_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.RETURN) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.LP) | (1 << D96Parser.LB) | (1 << D96Parser.LSB) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.ZERO_INTLIT) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLARID))) != 0):
                self.state = 189
                self.cons_des_stmt()
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list_with_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Id_list_with_typeContext)
            else:
                return self.getTypedRuleContext(D96Parser.Id_list_with_typeContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = D96Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.id_list_with_type()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 196
                self.match(D96Parser.SEMI)
                self.state = 197
                self.id_list_with_type()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_list_with_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids_list(self):
            return self.getTypedRuleContext(D96Parser.Ids_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_id_list_with_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list_with_type" ):
                return visitor.visitId_list_with_type(self)
            else:
                return visitor.visitChildren(self)




    def id_list_with_type(self):

        localctx = D96Parser.Id_list_with_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_id_list_with_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.ids_list()
            self.state = 204
            self.match(D96Parser.COLON)
            self.state = 205
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_ids_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds_list" ):
                return visitor.visitIds_list(self)
            else:
                return visitor.visitChildren(self)




    def ids_list(self):

        localctx = D96Parser.Ids_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ids_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(D96Parser.ID)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 208
                self.match(D96Parser.COMMA)

                self.state = 209
                self.match(D96Parser.ID)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def arr_type(self):
            return self.getTypedRuleContext(D96Parser.Arr_typeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_type_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = D96Parser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_type_name)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.arr_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arr_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_type" ):
                return visitor.visitArr_type(self)
            else:
                return visitor.visitChildren(self)




    def arr_type(self):

        localctx = D96Parser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(D96Parser.ARRAY)
            self.state = 223
            self.match(D96Parser.LSB)
            self.state = 224
            self.type_name()
            self.state = 225
            self.match(D96Parser.COMMA)
            self.state = 226
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 227
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cons_des_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_declareContext,0)


        def assignment(self):
            return self.getTypedRuleContext(D96Parser.AssignmentContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(D96Parser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def method_invoc_stmt(self):
            return self.getTypedRuleContext(D96Parser.Method_invoc_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_cons_des_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCons_des_stmt" ):
                return visitor.visitCons_des_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cons_des_stmt(self):

        localctx = D96Parser.Cons_des_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cons_des_stmt)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.var_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 233
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 234
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 235
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 236
                self.method_invoc_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 237
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_declareContext,0)


        def assignment(self):
            return self.getTypedRuleContext(D96Parser.AssignmentContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(D96Parser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def method_invoc_stmt(self):
            return self.getTypedRuleContext(D96Parser.Method_invoc_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.var_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 245
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 246
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 247
                self.method_invoc_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 248
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = D96Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 252
            self.match(D96Parser.ID)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 253
                self.match(D96Parser.COMMA)
                self.state = 254
                self.match(D96Parser.ID)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
            self.match(D96Parser.COLON)
            self.state = 261
            self.type_name()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 262
                self.match(D96Parser.ASSIGN)
                self.state = 263
                self.exp_list()


            self.state = 266
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def assign_rhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_rhsContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = D96Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.assign_lhs()
            self.state = 269
            self.match(D96Parser.ASSIGN)
            self.state = 270
            self.assign_rhs()
            self.state = 271
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def index(self):
            return self.getTypedRuleContext(D96Parser.IndexContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DOUBLECOLON(self):
            return self.getToken(D96Parser.DOUBLECOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs" ):
                return visitor.visitAssign_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign_lhs)
        self._la = 0 # Token type
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLARID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.operands()
                self.state = 275
                self.index()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.exp()
                self.state = 278
                self.match(D96Parser.DOT)
                self.state = 279
                self.match(D96Parser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.match(D96Parser.ID)
                self.state = 282
                self.match(D96Parser.DOUBLECOLON)
                self.state = 283
                self.match(D96Parser.DOLLARID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 284
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_rhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_rhs" ):
                return visitor.visitAssign_rhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_rhs(self):

        localctx = D96Parser.Assign_rhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assign_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def elseif_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Elseif_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Elseif_stmtContext,i)


        def else_stmt(self):
            return self.getTypedRuleContext(D96Parser.Else_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(D96Parser.IF)
            self.state = 290
            self.match(D96Parser.LP)
            self.state = 291
            self.exp()
            self.state = 292
            self.match(D96Parser.RP)
            self.state = 293
            self.block_stmt()
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 294
                self.elseif_stmt()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 300
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = D96Parser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(D96Parser.ELSEIF)
            self.state = 304
            self.match(D96Parser.LP)
            self.state = 305
            self.exp()
            self.state = 306
            self.match(D96Parser.RP)
            self.state = 307
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = D96Parser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(D96Parser.ELSE)
            self.state = 310
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def DOTDOT(self):
            return self.getToken(D96Parser.DOTDOT, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = D96Parser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(D96Parser.FOREACH)
            self.state = 313
            self.match(D96Parser.LP)
            self.state = 314
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLARID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 315
            self.match(D96Parser.IN)
            self.state = 316
            self.exp()
            self.state = 317
            self.match(D96Parser.DOTDOT)
            self.state = 318
            self.exp()
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 319
                self.match(D96Parser.BY)
                self.state = 320
                self.exp()


            self.state = 323
            self.match(D96Parser.RP)
            self.state = 324
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(D96Parser.BREAK)
            self.state = 327
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(D96Parser.CONTINUE)
            self.state = 330
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(D96Parser.RETURN)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.LP) | (1 << D96Parser.LSB) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.ZERO_INTLIT) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLARID))) != 0):
                self.state = 333
                self.exp()


            self.state = 336
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invoc_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def instance_method(self):
            return self.getTypedRuleContext(D96Parser.Instance_methodContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLECOLON(self):
            return self.getToken(D96Parser.DOUBLECOLON, 0)

        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invoc_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invoc_stmt" ):
                return visitor.visitMethod_invoc_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invoc_stmt(self):

        localctx = D96Parser.Method_invoc_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_method_invoc_stmt)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.exp()
                self.state = 339
                self.match(D96Parser.DOT)
                self.state = 340
                self.instance_method()
                self.state = 341
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.match(D96Parser.ID)
                self.state = 344
                self.match(D96Parser.DOUBLECOLON)
                self.state = 345
                self.static_method()
                self.state = 346
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(D96Parser.LB)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.RETURN) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.LP) | (1 << D96Parser.LB) | (1 << D96Parser.LSB) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.ZERO_INTLIT) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLARID))) != 0):
                self.state = 351
                self.stmt()
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 357
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(D96Parser.NEQ, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = D96Parser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NEQ) | (1 << D96Parser.LT) | (1 << D96Parser.GT) | (1 << D96Parser.LTE) | (1 << D96Parser.GTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp1Context,i)


        def CONCATSTR(self):
            return self.getToken(D96Parser.CONCATSTR, 0)

        def EQSTR(self):
            return self.getToken(D96Parser.EQSTR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.exp1()
                self.state = 362
                _la = self._input.LA(1)
                if not(_la==D96Parser.EQSTR or _la==D96Parser.CONCATSTR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 363
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp2Context,i)


        def relational(self):
            return self.getTypedRuleContext(D96Parser.RelationalContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = D96Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp1)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.exp2(0)
                self.state = 369
                self.relational()
                self.state = 370
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 378
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 379
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 380
                    self.exp3(0) 
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 389
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 390
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 391
                    self.exp4(0) 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MODULO(self):
            return self.getToken(D96Parser.MODULO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 402
                    self.exp5() 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp5)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.match(D96Parser.NOT)
                self.state = 409
                self.exp5()
                pass
            elif token in [D96Parser.SELF, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SUB, D96Parser.LP, D96Parser.LSB, D96Parser.INTEGER_LITERAL, D96Parser.ZERO_INTLIT, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID, D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp6)
        try:
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(D96Parser.SUB)
                self.state = 414
                self.exp6()
                pass
            elif token in [D96Parser.SELF, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.ARRAY, D96Parser.NEW, D96Parser.LP, D96Parser.LSB, D96Parser.INTEGER_LITERAL, D96Parser.ZERO_INTLIT, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID, D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.exp7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def index(self):
            return self.getTypedRuleContext(D96Parser.IndexContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 421
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 422
                    self.index() 
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 436
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 431
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 432
                    self.match(D96Parser.DOT)
                    self.state = 433
                    self.exp9(0) 
                self.state = 438
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def DOUBLECOLON(self):
            return self.getToken(D96Parser.DOUBLECOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 442
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 443
                    self.match(D96Parser.DOUBLECOLON)
                    self.state = 444
                    self.exp10() 
                self.state = 449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp10)
        try:
            self.state = 453
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(D96Parser.NEW)
                self.state = 451
                self.exp10()
                pass
            elif token in [D96Parser.SELF, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.ARRAY, D96Parser.LP, D96Parser.LSB, D96Parser.INTEGER_LITERAL, D96Parser.ZERO_INTLIT, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID, D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def instance_method(self):
            return self.getTypedRuleContext(D96Parser.Instance_methodContext,0)


        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def index(self):
            return self.getTypedRuleContext(D96Parser.IndexContext,0)


        def obj_create(self):
            return self.getTypedRuleContext(D96Parser.Obj_createContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_operands)
        self._la = 0 # Token type
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.instance_method()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                self.static_method()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 458
                self.index()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 459
                self.obj_create()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 460
                self.match(D96Parser.LP)
                self.state = 461
                self.exp()
                self.state = 462
                self.match(D96Parser.RP)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 464
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLARID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index(self):
            return self.getTypedRuleContext(D96Parser.IndexContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = D96Parser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_index)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.match(D96Parser.LSB)
                self.state = 468
                self.exp()
                self.state = 469
                self.match(D96Parser.RSB)
                self.state = 470
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.match(D96Parser.LSB)
                self.state = 473
                self.exp()
                self.state = 474
                self.match(D96Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method" ):
                return visitor.visitInstance_method(self)
            else:
                return visitor.visitChildren(self)




    def instance_method(self):

        localctx = D96Parser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_instance_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(D96Parser.ID)
            self.state = 479
            self.match(D96Parser.LP)
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.LP) | (1 << D96Parser.LSB) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.ZERO_INTLIT) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLARID))) != 0):
                self.state = 480
                self.exp_list()


            self.state = 483
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method" ):
                return visitor.visitStatic_method(self)
            else:
                return visitor.visitChildren(self)




    def static_method(self):

        localctx = D96Parser.Static_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(D96Parser.DOLLARID)
            self.state = 486
            self.match(D96Parser.LP)
            self.state = 488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.LP) | (1 << D96Parser.LSB) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.ZERO_INTLIT) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLARID))) != 0):
                self.state = 487
                self.exp_list()


            self.state = 490
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_createContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_obj_create

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_create" ):
                return visitor.visitObj_create(self)
            else:
                return visitor.visitChildren(self)




    def obj_create(self):

        localctx = D96Parser.Obj_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_obj_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(D96Parser.ID)
            self.state = 493
            self.match(D96Parser.LP)
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.LP) | (1 << D96Parser.LSB) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.ZERO_INTLIT) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLARID))) != 0):
                self.state = 494
                self.exp_list()


            self.state = 497
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = D96Parser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_exp_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 499
                    self.exp()
                    self.state = 500
                    self.match(D96Parser.COMMA) 
                self.state = 506
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

            self.state = 507
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def ZERO_INTLIT(self):
            return self.getToken(D96Parser.ZERO_INTLIT, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(D96Parser.Array_literalContext,0)


        def boolean_literal(self):
            return self.getTypedRuleContext(D96Parser.Boolean_literalContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literal)
        try:
            self.state = 517
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.ZERO_INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                self.match(D96Parser.ZERO_INTLIT)
                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 511
                self.match(D96Parser.FLOAT_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 512
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 513
                self.array_literal()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 514
                self.boolean_literal()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 7)
                self.state = 515
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 516
                self.match(D96Parser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = D96Parser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            _la = self._input.LA(1)
            if not(_la==D96Parser.TRUE or _la==D96Parser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def array_literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Array_literalContext)
            else:
                return self.getTypedRuleContext(D96Parser.Array_literalContext,i)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.state = 539
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.match(D96Parser.ARRAY)
                self.state = 522
                self.match(D96Parser.LP)
                self.state = 523
                self.array_literal()
                self.state = 528
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 524
                    self.match(D96Parser.COMMA)
                    self.state = 525
                    self.array_literal()
                    self.state = 530
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 531
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.match(D96Parser.ARRAY)
                self.state = 534
                self.match(D96Parser.LP)
                self.state = 536
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.LP) | (1 << D96Parser.LSB) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.ZERO_INTLIT) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLARID))) != 0):
                    self.state = 535
                    self.exp_list()


                self.state = 538
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[35] = self.exp2_sempred
        self._predicates[36] = self.exp3_sempred
        self._predicates[37] = self.exp4_sempred
        self._predicates[40] = self.exp7_sempred
        self._predicates[41] = self.exp8_sempred
        self._predicates[42] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




