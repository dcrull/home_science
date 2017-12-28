# home_science
Repo for working experiments around the home.

## RESEARCH PROJECT #1: Unsupervised classification and event detection for environmental sensors (temp, humidity, barometry)

***Primary inquiry: Can we develop an unsupervised classification model that consistently (and accurately) predicts classes or “states” of the natural environment as determined by sensor data?***

Secondary inquiry: How do we define accurate prediction or ground truth with unsupervised methods? I.e. In conventional unsupervised learning, the classes/labels are not available for training, but are still used in model evaluation. How is such validation done when the classes/labels do not exist explicitly?

* A note on ensemble validation approach: Individual optimized models (Step 1) may end up performing well on test data and demonstrate that they are self-consistent according to our validation metrics. This is useful in terms of prediction (if it works), but more useful would be the ability to demonstrate that an ensemble of classifiers are not only self-consistent but in agreement with each other on classification. This agreement might indicate natural structure in the data.

### Data
-	Sensor data collected on:
-	Temperature (primary)
-	Humidity (primary)
- Barometry (primary)
-	Luminosity
-	Sound (amplitude at a certain sample rate)
-	Particle detection

-	Collected continuously initially indoors at home (future experiments should leverage multiple external locations)

### Methods 
The following are possible methods to implement - I’ll seek NYU/CUSP guidance on narrowing this w.r.t. the research goals.
-	Unsupervised machine learning
-	Cluster analysis
-	K-means
-	Gaussian Mixture Models
-	DBSCAN
-	Hierarchical clustering
-	Self-Organizing Maps (SOM) (lit here using SOM on sleep sounds, more on SOM)
-	Neural networks
-	Deep belief networks (literature here on use in computer vision - transferrable?) 
-	Recurrent Neural Networks (lit here)
-	Lit here on using NN with sensor data
-	Naive Bayes classifier
 
### Key considerations for experimental design
Hypotheses framed around comparing these categories of factors

-	Feature engineering and parameterization techniques 
-	What features / combos of features work best?
-	Signal processing techniques like spectrograms, DFT, documenting basic distribution info (mean, variance over sample period...what sample period is best, etc)
-	Are abstracted features (i.e. through higher dimensions using kernel processes, etc) effective?
-	Should basic data pre-processing be included as an experimental factor?
-	Data and training
-	Comparison across modes (temp., light, sound, etc)
-	Sample size for training/cross-validation
-	Characterize as time series?
-	What cross-validation approach? (probably K-folds)
-	***What validation criteria?*** Key to secondary research question
-	Internal vs external validation techniques (survey on internal and external indexes here)
-	Internal: cluster stability (compared across training/cross-validation)
-	Internal: intra-group similarity and inter-group contrast/separation
-	Jaccard similarity/distance?
-	KL divergence (i.e. relative entropy)?
-	Statistical tests of distributions?
-	External??
-	Ensemble validation approach:
-	Step 1: Optimize individual model hyper-parameters for model selection and tuning (using validation techniques proposed above for each model). Does each model group data consistently and distinctly?
-	Step 2: Compare the model clusters with other model clusters (using Jaccard similarity / KL divergence, etc) and determine if there is significant “ensemble agreement” among models

### Testing
-	Run test data against models that are optimized both individually and as an ensemble and determine if the stability/consistency/similarities hold true on test data
-	Since the data is being tested continuously, this provides new opportunities to re-train/cross-validate and test

### Key hardware / engineering considerations
-	Hardware: commodity sensors controlled by RPi3 processor; SD Card data storage
-	Data processing / computing resources
-	Collection, aggregation, and pre-processing in situ
-	However, training dataset will likely need to be collected and used retroactively - cross-validation techniques seem really complicated in a streaming/online learning scenario (but note for future research)
-	Testing and evaluation (perhaps some model/parameter tuning) can occur in real-time in situ
-	Virtual environment (I found an RPI emulator and am testing it, could be helpful for testing various pre-processing and ML scripts virtually before trying on device)
-	Sensor data
-	Ultimate goal is use in the field, so will plan to use the same sensors as deployed in external locations, but might consider additions if feature engineering / model training hits a wall

### Methodology
1A. Create testable groups of:
  -	 Features from the data
  -  ML models
  -	 Model hyper-parameters (e.g. learning rate, regularization, etc)
  -	 Validation techniques

1B. Build sensor cluster with Raspberry Pi and start collecting raw data

2. Develop data pre-processing scripts for RPi as appropriate (once there’s a plan for what features to analyze)

3. Train and cross-validate data
  -	Objective: What are the optimal features, models, and parameters needed to achieve acceptable cluster validation? (i.e. stability, similarity, ensemble agreement, etc)

4. Once the objective of Step 3 has been met, test on new data (i.e. newly collected sensor data). Two broad outcomes:
-	Models fail to meet validation threshold on test data….back to the drawing board (need more data? Different features or models?)
-	Models succeeds in meeting validation threshold:
    -	Analyze properties of the emergent classes the models produce by empirical/observable features and statistical analysis
    -	Applied research: repeat in external locations (ultimately trying to establish a baseline classification schema that could be used to detect trends, anomalies, etc)
    -	Continue functional research: add more sensors/types of sensor data; determine if this can be used for sensor diagnostics, etc.
