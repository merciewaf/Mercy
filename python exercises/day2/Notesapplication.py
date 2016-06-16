class NotesApplication(object):
	def __init__(self, author,notes_lists):
		self.author=author
		self.notes_lists=[]

	def create(self, note_content):
		self.notes_lists.append(note_content)

	def list(self):
		for notes in self.notes_list:
			print("Note ID: {0}\n {1}\n By author {2}".format(self.notes_lists.index(notes),notes,self.author))
	def get_note_id(self, note_id):
		return self.notes_lists[note_id]

	def search(self, search_text):
		search_list = [content for content in self.notes_list if search_text in content]
		if len(search_list)>0:
			print("showing results for search %s"%search_text)
			for notes in search_list:
				print("Note ID: {0}\n {1}\n By author {2}".format(self.notes_list.index(notes),notes,self.author))
	
	def edit(self, note_id, new_content):
		self.notes_lists[note_id]=new_content
		return self.notes_list

a=NotesApplication()
a.create()
a.list()
a.get_note_id()
a.search()
a.edit()
