import storage
from bin_convert import HalfPrecision

class Access:
	@staticmethod
	def data(addr,flow=["var"]):
		for typ in flow:
			var = storage.variable
			if typ.lower()=="mem" or typ.lower()=="memory":
				var = storage.memory
			elif typ.lower()=="reg" or typ.lower()=="register":
				var = storage.register
			addr = var.load(addr)
		return addr
	def store(typ,addr,value):

class AddressingMode:
	@staticmethod
	def immediate(var):
	def relative(displace):
	def based(displace):
	def indexed(displace):
	def register(reg_addr):
	def register_indirect(reg_addr):
	def direct(var_addr):
	def indirect(var_addr):
	def autoinc(reg_addr):
	def autodec(reg_addr):

