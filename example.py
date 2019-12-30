from fluidchain.core import FluidChain
from fluidchain.objects import FluidNMF, FluidHPSS, FluidTransients


chain = FluidChain()

# Define your 'links'
nmf = FluidNMF()
transients = FluidTransients()
hpss = FluidHPSS()

# Now we create the chain
chain.source('/Users/james/testaudio.wav')
chain.outpath('/Users/james/dev/fluid/FluidChain/output_tests/')
chain.add(hpss)
chain.add(transients)
chain.add(nmf)
chain.run()