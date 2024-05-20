import sys
import compiler
from addressing import Access, AddressingMode
import storage
from bin_convert import HalfPrecision, Length


class Program:
	def __init__(self, program):
		pass

	def run(self) -> None:
		monadic = []
		niladic = []

		ir = storage.register.load("IR")
		pc = storage.register.load("PC")

		while True:
                        if len(str(ir)) != 32 or ir == 0:
				break
			opcode_mask = 0b11111 << 27  # 11111 0 000 0000000 0 000 0000000 00000
			operand1_mask = 0b1111111 << 16	 # 00000 0 000 1111111 0 000 0000000 00000
			operand2_mask = 0b1111111 << 5		# 00000 0 000 0000000 0 000 1111111 00000
			comcode_mask = 0b00111 << 27  # 00111 0 000 0000000 0 000 0000000 00000

			# Looping and getting the OpCode and the operands as well as updating the ‘IR’ and ‘PC’ in the run method of the
			#  Program class from run.py.

			opcode = str((ir & opcode_mask))
			operand1_address: int = (ir & operand1_mask) >> 16
			operand2_address: int = (ir & operand2_mask) >> 5

			# fetch
			# decode

			# execute
			# write
			# no execute, no store
			if opcode[0:2] == "00":
				comcode = int(opcode[2:5], 2)
				if comcode == 0:  # PRNT
					br = Access.data("BR", ["var", "reg"])
					print_msg = storage.variable.data["MSG"][ir-br]
					msg_val = ""
					if result[0] != 0:
						msg_val = str(result[0])
				print(print_msg+" "+msg_val)
			ir = pc
			pc += 1

			# next instruction
	def getOp(self,inscode):
		pass

	def execute(self,result,opcode):
		pass

	def write(self,dest,src,movcode):

		# SCAN
		print_msg = storage.variable.data["MSG"][ir-br]
		src = HalfPrecision.hpdec2bin(float(input(print_msg+": ")))


	@staticmethod
	def exception(name,value):
		pass


class Except:
	pass
#run program
