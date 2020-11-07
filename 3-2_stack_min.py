'''
A time efficient solution would be to keep an extra attribute of each node which states the minimum below that node in the stack,
so that whenever elements are popped we have access to the min of the substack (min property of the top node)
'''