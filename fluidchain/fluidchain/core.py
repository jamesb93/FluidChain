class FluidChain():
    """
    Container which you add links to.
    A chain represents a kind of 'dsp chain.
    """
    def __init__(self):
        self.file_buffer = []
        self.sink = ""
        self.links = []
        self.counter = 0
    
    def source(self, file_path):
        self.file_buffer.append(file_path)
    
    def outpath(self, folder_path):
        self.sink = folder_path

    def add(self, object_name):
        self.links.append(object_name)
        object_name.input = self.file_buffer
        object_name.process_params(self)
        self.file_buffer = object_name.output
        self.counter += 1
    
    def run(self):
        for link in self.links:
            print(f'Processing {link.name}')
            link.process()




