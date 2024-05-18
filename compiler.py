import storage
from addressing import Access, AddressingMode
from bin_convert import Length, HalfPrecision

operations = [["MOD","ADD","SUB","MUL","DIV"],["JEQ","JNE","JLT","JLE","JGT","JGE","JMP"],["MOV","CALL","RET","SCAN"],["PRNT","EOP"]]
operationCodes = [["11","10","01","00"],["000","001","010","011","100","101","110","111"]]
class Instruction:
	@staticmethod
	def encode(inst):
	def encodeOp(operand):
		if 'M:' in operand:	#message for printing and scanning
			msg = Instruction.decodeMSG(operand.replace("M:",""))
			storage.variable.data["MSG"][storage.variable.data["MI"]] = msg
			return "".zfill(Length.operand)
		else:
	def encodeProgram(program):
			block_addr = br+len(inst_list)-block_i
			storage.variable.data["MI"] = block_addr
	def decodeMSG(msg):
		msg = msg.replace("-_","\n").replace("_","\t").replace("-"," ")
		return msg.replace("minus","-").replace("under","_")
