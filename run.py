import sys
import compiler
from addressing import Access, AddressingMode
import storage
from bin_convert import HalfPrecision, Length

class Program:
	def __init__(self,program):
	def run(self):
		monadic = []
		niladic = []
			#fetch
			#decode
			#execute
			#write
			#no execute, no store
			if opcode[0:2]=="00":
				comcode = int(opcode[2:5],2)
				if comcode==0: #PRNT
					br = Access.data("BR",["var","reg"])
					print_msg = storage.variable.data["MSG"][ir-br]
					msg_val = ""
					if result[0]!=0:
						msg_val = str(result[0])
					print(print_msg+" "+msg_val)
			#next instruction
	def getOp(self,inscode):
	def execute(self,result,opcode):
	def write(self,dest,src,movcode):
		#SCAN
			print_msg = storage.variable.data["MSG"][ir-br]
			src = HalfPrecision.hpdec2bin(float(input(print_msg+": ")))
	@staticmethod
	def exception(name,value):
class Except:

#run program
