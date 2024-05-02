# Model Summary

Provide a brief overview of the model including details about its architecture, how it can be used, characteristics of the model, training data, and evaluation results.

## Usage

How can this model be used? You should provide a code snippet that demonstrates how to load and/or fine-tune your model, and you should define the shape of both the inputs and the outputs.  Are there known and preventable failures to be aware of?

## System

Is this a standalone model or part of a system? What are the input requirements? What are the downstream dependencies when using the model outputs?

## Implementation requirements

What hardware and software were used for training the model? Describe the compute requirements for training and inference (e.g., # of chips, training time, total computation, measured performance, energy consumption).

# Model Characteristics

## Model initialization

Was the model trained from scratch or fine-tuned from a pre-trained model?

## Model stats

What’s the size of the model? Provide information about size, weights, layers, and latency.

## Other details

Is the model pruned? Is it quantized? Describe any techniques to preserve differential privacy.

# Data Overview

Provide more details about the data used to train this model.

## Training data

Describe the data that was used to train the model. How was it collected? What pre-processing was done?

## Demographic groups

Describe any demographic data or attributes that suggest demographic groups

## Evaluation data

What was the train / test / dev split? Are there notable differences between training and test data?

# Evaluation Results

## Summary

Summarize and link to evaluation results for this analysis.

## Subgroup evaluation results

Did you do any subgroup analysis? Describe the results and any assumptions about disaggregating data. Are there any known and preventable failures about this model?

## Fairness 

How did you define fairness? What metrics and baselines did you use? What were the results of your analysis?

## Usage limitations

Are there sensitive use cases? What factors might limit model performance and what conditions should be satisfied to use this model? 

## Ethics

What ethical factors did the model developers consider? Were any risks identified? What mitigations or remediates were undertaken?
