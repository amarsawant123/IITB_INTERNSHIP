# IITB_INTERNSHP

This report is based on the analysis of a unique and rich multimodal dataset titled "A 
Multisensor Dataset of South Asian Postgraduate Students Working on Mental Rotation 
Tasks." The dataset originates from a comprehensive cognitive science and affective 
computing research study aimed at exploring how postgraduate students solve complex spatial 
reasoning problems, specifically 3D mental rotation tasks. These types of problems are 
widely recognized as being mentally demanding and are frequently used in studies related to 
human cognition, spatial intelligence, and workload analysis. 
The core objective of the study was to gain deeper insights into the cognitive, emotional, 
and physiological states of students as they engage with mental rotation tasks under varying 
experimental conditions. By observing and recording multisensory data, the study seeks to 
reveal the internal mechanisms—such as stress response, focus, fatigue, and emotional 
shifts—that accompany problem-solving in cognitively intensive environments. 

#
Each of the eight participants (IDs 31 to 38) contributed a complete set of multimodal sensor 
data. These data streams were recorded synchronously to allow precise temporal alignment and 
cross-modal analysis. Below is an overview of the primary data files and their contents:

* EEG.csv: Contains brainwave signal amplitudes (Delta, Theta, Alpha, Beta, Gamma) 
measured from four electrodes (TP9, AF7, AF8, TP10). Includes raw EEG voltages, 
head movement (accelerometer/gyroscope), and device quality indicators.

* GSR.csv: Includes skin conductance and resistance measurements that serve as proxies 
for emotional arousal and physiological stress levels. 

* IVT.csv / EYE.csv: Provide high-frequency eye-tracking data, including gaze 
coordinates, fixation duration, saccades, and pupil size. These features help infer visual 
attention and scanning strategies. 

* TIVA.csv: Captures facial emotion probabilities (confusion, joy, engagement, 
frustration, etc.) along with action units and head pose data derived from webcam 
analysis using Affective SDK.PSY.csv: Records task performance details including 
task category (condition), difficulty, correctness, response time, and timestamps.

* NSTLX.csv: Contains self-reported workload measures for each session based on 
NASA-TLX metrics (mental demand, physical demand, effort, frustration, 
performance). 

* DLOT.xlsx: Observer-coded behavioural annotations made every 10 seconds to log 
engagement, confusion, and other notable expressions. 

* ExternalEvents.csv & BlankScreenData.csv: Document slide transitions, rest 
periods, and visual stimuli intervals, useful for synchronizing task phases with 
physiological recordings. 

The dataset for each participant exceeds 1 million records and spans approximately 800MB in 
total volume. This ensures a rich foundation for multimodal modelling and analysis. 
