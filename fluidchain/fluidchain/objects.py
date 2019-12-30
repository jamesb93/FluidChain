import uuid, subprocess, os

class FluidProcessor():
    def __init__(self):
        self.input = []
        self.output = []
        self.cmd = []

    def process(self):
        for command in self.cmd:
            subprocess.call(command)

class FluidNMF(FluidProcessor):
    def __init__(self):
        self.name = 'nmf'
        self.fftsettings = (4096, 1024, 4096)
        self.components = 2
        self.iterations = 100
        self.outputs = [
            'resynth'
        ]
        FluidProcessor.__init__(self)
    
    def process_params(self, chain):
        for i in self.input:
            output_string = f'{chain.counter}_{self.name}_{self.outputs[0]}_{uuid.uuid4().hex[:6]}.wav'
            output_string = os.path.join(chain.sink, output_string)
            self.output.append(output_string)
            self.cmd.append([
                'fluid-nmf',
                '-source', str(i),
                f'-{self.outputs[0]}', output_string,
                '-fftsettings', str(self.fftsettings[0]), str(self.fftsettings[1]), str(self.fftsettings[2]),
                '-iterations', str(self.iterations),
                '-components', str(self.components)
            ])

class FluidHPSS(FluidProcessor):
    def __init__(self):
        self.name = 'hpss'
        self.fftsettings = (4096, 1024, 4096)
        self.harmfiltersize = 17
        self.percfiltersize = 31
        self.outputs = [
            'harmonic',
            'percussive'
        ]
        FluidProcessor.__init__(self)
    
    def process_params(self, chain):
        for i in self.input:
            harm_out = f'{chain.counter}_{self.name}_{self.outputs[0]}_{uuid.uuid4().hex[:6]}.wav'
            harm_out = os.path.join(chain.sink, harm_out)
            perc_out = f'{chain.counter}_{self.name}_{self.outputs[1]}_{uuid.uuid4().hex[:6]}.wav'
            perc_out = os.path.join(chain.sink, perc_out)
            self.output.append(harm_out)
            self.output.append(perc_out)
            self.cmd.append([
                'fluid-hpss',
                '-source', str(i),
                f'-{self.outputs[0]}', harm_out,
                f'-{self.outputs[1]}', perc_out,
                '-fftsettings', str(self.fftsettings[0]), str(self.fftsettings[1]), str(self.fftsettings[2]),
                '-harmfiltersize', str(self.harmfiltersize),
                '-percfiltersize', str(self.percfiltersize)
            ])

class FluidTransients(FluidProcessor):
    def __init__(self):
        self.name = 'transi'
        self.blocksize = 256
        self.clumplength = 25
        self.order = 20
        self.padsize = 128
        self.skew = 0.0
        self.threshback = 1.1
        self.threshfwd = 2.0
        self.windowsize = 14
        self.outputs = [
            'transients',
            'residual',
        ]
        FluidProcessor.__init__(self)
    
    def process_params(self, chain):
        for i in self.input:
            trans_out = f'{chain.counter}_{self.name}_{self.outputs[0]}_{uuid.uuid4().hex[:6]}.wav'
            trans_out = os.path.join(chain.sink, trans_out)
            resid_out = f'{chain.counter}_{self.name}_{self.outputs[1]}_{uuid.uuid4().hex[:6]}.wav'
            resid_out = os.path.join(chain.sink, resid_out)
            self.output.append(trans_out)
            self.output.append(resid_out)
            self.cmd.append([
                'fluid-transients',
                '-source', str(i),
                f'-{self.outputs[0]}', trans_out,
                f'-{self.outputs[1]}', resid_out,
                '-blocksize', str(self.blocksize),
                '-clumplength', str(self.clumplength),
                '-order', str(self.order),
                '-padsize', str(self.padsize),
                '-skew', str(self.skew),
                '-threshback', str(self.threshback),
                '-threshfwd', str(self.threshfwd),
                '-windowsize', str(self.windowsize)
            ])