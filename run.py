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

			opcode_mask = 0b11111 << 27  # 11111 0 000 0000000 0 000 0000000 00000
			operand1_mask = 0b1111111 << 16	 # 00000 0 000 1111111 0 000 0000000 00000
			operand2_mask = 0b1111111 << 5		# 00000 0 000 0000000 0 000 1111111 00000
			comcode_mask = 0b00111 << 27  # 00111 0 000 0000000 0 000 0000000 00000

			# Looping and getting the OpCode and the operands as well as updating the ‘IR’ and ‘PC’ in the run method of the
			#  Program class from run.py.

			opcode = (ir & opcode_mask)
			operand1 = (ir & operand1_mask)
			operand2 = (ir & operand2_mask)

			# fetch
			# decode

			# execute
			self.execute(result,opcode)
			# write
			# no execute, no store
			if str(opcode[0:2]) == "00":
				comcode: int = opcode & comcode_mask
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
		category_code: dict = {"MOD": 0b000, "ADD": 0b001, "SUB": 0b010, "MUL": 0b011, "DIV": 0b100}
		category_code_mask = 0b111
		write_bit_mask = 0b10000
		if opcode & write_bit_mask == 0b10000:

			if(opcode & category_code_mask == category_code["MOD"]):
				result = result[0] % result[1]

			return
		else:
			return


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
