# Optimizer

A tutorial for instalation and use can be found [here](http://clients.teksavvy.com/~nickm/scripts/nec_opt_tutorial.html).

This folder contains the optimizer's scripts and a template to optimize a Yagi antenna with 6 elements.

## Template: input.nec
#### The target function needs to be set. For example:

``` CMD--OPT --target-function=max_gain_diff```

The optimizer will minimize the difference between the target net gain and the current net gain. Your target function also needs to handle the SWR and F2B with proper weights. All target function options can be found [here](http://clients.teksavvy.com/~nickm/scripts.html#nec_opt).

#### The geometry limits need to be set. For example:

```SY REF_Z=0.15' 0.1, 0.25```

The length of the reflector will start with 15cm, and its lower and upper boundary will be 10cm and 25cm, respectively.

## CMD commands:
Optimize command:

```python -m nec.opt input.nec```

Evaluate command:

```python -m nec.eval output_file_name.nec ```

## Results
After evaluation, an HTML file is created. It contains:

### The numerical results:
![](https://i.imgur.com/lgXT0zS.png)

### The plot of directivity (raw gain), net gain and SWR:
![](https://i.imgur.com/be50iO9.png)

### The radiation pattern:
![](https://i.imgur.com/RP9scvH.png)


