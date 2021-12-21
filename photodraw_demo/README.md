# Visual communication of object concepts at different levels of abstraction (DEMO)

This folder contains code used to demonstrate a minimally working experiment of the Photodraw project (submitted to Cogsci 2021 in the paper, Yang \& Fan, 2021). This demo can be downloaded and run locally by double clicking the "index.html" file, which will open in your default browser.

In the below, you may download the full stimuli set and data used in the experiments and analysis notebooks.  

<p align="center" style="font-size: smaller">
  <img width="85%" src="https://github.com/cogtoolslab/photodraw32/blob/master/experiments/instancedraw_photo/stimuli/instance_photo_screencap.gif"></img><br/>
</p>

1. [Stimuli](#stimuli)
2. [Experiments](#experiments)
3. [Download data](#download-entire-dataset)
4. [Analysis](#analysis)

-----

## Stimuli

**Recommended**:[Link to download our stimuli (116 MB)](https://photodraw32-public.s3.amazonaws.com/stimuli.zip).

The `stimuli` directory contains code used to prepare our stimulus set for web experiments. For full information, see [the stimuli directory](https://github.com/cogtoolslab/photodraw32/tree/master/stimuli). The zipped stimulus set contains PNGs of all 12 images presented to participants in the `photodraw_pilot` study and all `1024` images presented to participants in the `photodraw32` study, divided into categories.

`NOTE: running download_data.py downloads the stimuli folders and files that would have been created by running the files in /stimuli.`

<p align="center" style="font-size: smaller">
  <img width="100%" src="https://github.com/cogtoolslab/photodraw32/blob/master/results/plots/photodraw32_cats.png"></img><br/>
  All photo-cue cat stimuli in photodraw32 experiment, sorted by participant-rated typicality
</p>


## Experiments

We ran a series of experiments examining how sensory information and representational goals jointly constrain the content and form of our drawings. The details of the experimental design and data exclusion procedures are documented in this [study preregistration](https://docs.google.com/document/d/18pjh5C2YJFB5ht_hXGUqKW8uXivLukPgXDTqhO5YkPU/edit?usp=sharing). In our pilot experiment (`experiments/photodraw_pilot`) participants produced a total of 12 drawings, corresponding to 12 familiar basic-level categories, where 6 drawings were cued using a category label and the other 6 were cued using a typical exemplar from that category.

In the second experiment (`photodraw32`) we independently manipulated sensory information (photo/text cue type) and representaional goals (to draw an exemplar vs. a category) to form a 2x2 factorial design. This time, participants drew 32 drawings corresponding, to 32 basic-level categories.

The individual subdirectories within `/experiments` provide greater detail on the implementation of the experiments.

<p align="center" style="font-size: smaller">
  <img width="75%" src="https://github.com/cogtoolslab/photodraw32/blob/master/results/plots/photodraw32_gallery.png"></img><br/>
  Example cues and drawings in photodraw32 task
</p>


## Download entire dataset

Running the script `download_data.py` in the home directory `/photodraw32` will download tidy `*.csv` files, all participant sketches, experiment metadata, gallery files, and plots for browsing (**1.9 GB**).

[Link to download the tidy formatted datasets (182 MB)](https://photodraw32-public.s3.amazonaws.com/datasets.zip)<br>
[Link to download model features (189 MB)](https://photodraw32-public.s3.amazonaws.com/features.zip)  (may not be included in public release)<br>
[Link to download PNGs of all sketches (94 MB)](https://photodraw32-public.s3.amazonaws.com/sketches.zip)<br>


## Analysis

The `/analysis` directory contains code used to analyze the data generated from our experiments. The directory can be categorized into a few main components. `*_photodraw32.ipnyb` and `*_photodraw32_R.Rmd` files contain the main analyses and plots reported in the paper. Files in `/analysis/preprocessing` are used to process the raw data and convert them into tidy dataframes, while files in `*/analysis/supplemental` files contain supplemental analyses not reported in the paper. Greater detail describingthe individual analysis files can be found in the [analysis directory](https://github.com/cogtoolslab/photodraw32/tree/master/analysis).

<p align="center" style="font-size: smaller">
  <br/>
  <img width="95%" src="https://github.com/cogtoolslab/photodraw32/blob/master/results/plots/photodraw32_results.png"></img><br/>
  Main results of photodraw32
</p>
