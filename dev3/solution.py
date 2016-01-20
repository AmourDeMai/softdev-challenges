import gdb
import copy

class ReadCommand(gdb.Command):

	def __init__(self):
		super(ReadCommand, self).__init__("pstruct", gdb.COMMAND_DATA)

	def printFields(self, addr, fields):
		print '-------------'
		if 'n' in fields:
			self.printFieldWithN(addr, fields)
		else:
			for i in range(len(fields)):
				addr = self.printAField(addr, fields, i)
			print '-------------'
		print ""

	def printFieldWithN(self, addr, fields):
		'''function to traite when the fields includes 'n' '''
		### first print all the field, then traite the pointer
		for i in range(len(fields)):
			if fields[i] != 'n':
				addr = self.printAField(addr, fields, i)
				### here will cause a bug in the case as "lin", because system will add 4 bytes
				### for int data in order to adapt to the prevois long data which has 8 bytes
				#if fields[i] == 'i' or fields[i] == 'f':
				#	addr = addr + 4		
				#print '[addr4]%02x' %  addr, '[addr type]', type(addr), type(addr) != 'int'
			else:
				nextAddr = addr
				addr = addr + 8	
				#print '[nextAddr]%02x' % nextAddr, '[addr type]', type(nextAddr)
		print '-------------'
		command = 'x/1ag' + hex(nextAddr)
		result = gdb.execute(command, False, True)
		nextP = result.split()[1]
		if nextP == '0x0':
			return
		else:
			nextP = int(nextP, 16)
			self.printFieldWithN(nextP, fields)

	def printAField(self, addr, fields, i):
		if fields[i] == 'i':
			command = "x/1dw" + hex(addr)
			result = gdb.execute(command, False, True)
			print ">", result.split()[1]
			return addr + 4
		elif fields[i] == 'l':
			command = "x/1dg" + hex(addr)
			result = gdb.execute(command, False, True)
			print ">", result.split()[1]
			return addr + 8
		elif fields[i] == 'f':
			command = "x/1fw" + hex(addr)
			result = gdb.execute(command, False, True)
			print ">", result.split()[1]
			return addr + 4
		elif fields[i] == 'p':
			command = "x/1ag" + hex(addr)
			result = gdb.execute(command, False, True)
			print ">", result.split()[1]
			return addr + 8
		elif fields[i] == 's':
			command = "x/1ag" + hex(addr)
			result = gdb.execute(command, False, True)
			contentAddr = result.split("\t")[1]
			command = "x/s" + str(contentAddr)
			result = gdb.execute(command, False, True)
			print ">", result.split()[1]
			return addr + 8
		elif fields[i] == '.':
			return addr + 4

	def invoke(self, arg, from_ppy):
		inferior = gdb.inferiors()[0]
		args = arg.split(" ")
		addr = int(args[0], 0)
		fields = str(args[1])
		self.printFields(addr, fields)

ReadCommand()
