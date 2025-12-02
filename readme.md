===========================================================================
ADAPTIVE TRAFFIC CONTROL WITH DEEP REINFORCEMENT LEARNING
===========================================================================

Introduction

The rapid increase in automobiles on roadways has naturally lead to traffic congestions all over the world, forcing drivers to sit idly in their cars wasting time and needlessly consuming fuel. Ride sharing and infrastructural improvements can help mitigate this but one of the key components to handling traffic congestion is traffic light timing. Traffic light control policies are often not optimized, leading to cars waiting pointlessly for nonexistent traffic to pass on the crossing road. We feel that traffic light control policy can be greatly improved by implementing machine learning concepts. Our project focuses on implementing a learning algorithm that will allow traffic control devices to study traffic patterns/behaviors for a given intersection and optimize traffic flow by altering stoplight timing. We do this with a Q-Learning technique, similarly seen in previous works such as Gao et. al. and Genders et. al, where  an intersection is knowledgeable of the presence of vehicles and their speed as they approach the intersection. From this information, the intersection is able to learn a set of state and action policies that allow traffic lights to make optimized decisions based on their current state. Our work seeks to alleviate traffic congestion on roads across the world by making intersections more aware of traffic presence and giving them the ability to take appropriate action to optimize traffic flow and minimize waiting time.

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)
Setup

This project was developed using python 3. Install from python.org .

Prerequisite Packages :
1) Tensorflow (pip install tensorflow) or (pip install tensorflow-gpu)
2) Keras (pip install keras)

The simulatons were done on SUMO Traffic Simulator. It is available at following location :- http://sumo.dlr.de/wiki/Downloads

Please refer to installation instructions of sumo from the website.



Running

Run file - traffic_light_control.py


Proposed System

3.1   Scope:

•	Traffic Flow Optimization:
ATSC aims to optimize traffic flow by dynamically adjusting signal timings in response to changing traffic conditions. This helps in reducing congestion, minimizing delays, and improving overall traffic efficiency.

•	Reducing Congestion:
One of the primary goals of ATSC is to alleviate congestion at intersections. By adapting signal timings based on real-time data, the system can reduce wait times and enhance the smooth movement of vehicles through intersections.

•	Environmental Impact:
ATSC can contribute to the reduction of fuel consumption and emissions by minimizing the time vehicles spend idling at intersections. This aligns with environmental goals and promotes sustainable urban transportation.

3.2	Objectives:

•	Review of Neural Network Applications in Traffic Management: 
Investigate the role of Neural Networks in traffic signal control, examining their capacity to model and predict traffic patterns, and assessing how their adaptive learning capabilities can contribute to dynamic signal optimization.

•	Assessment of System Performance and Efficiency: 
Evaluate the performance and efficiency gains achieved through the implementation of the adaptive traffic signal control system, measuring its impact on reducing congestion, improving traffic flow, and enhancing overall urban mobility.




•	Identification of Challenges and Limitations: 
Identify and analyze the challenges and limitations associated with the adoption of Neural Networks and DQN in traffic signal control systems, addressing issues such as computational complexity, data requirements, and potential uncertainties in real-world scenarios.


3.3 Work Flow Diagram :

 



3.3	Description:
To approach this problem, we use Q-Learning, where an agent, based on the given state, selects an appropriate action for the intersection in order to maximize present and future rewards. The state-action pairs, also called Q values, are learned and saved to a table where there values are continuously updated until convergence, where an ideal policy is found. This algorithm is outlined in more detail in the following sections.

Intersection Model:

                                                

We used the above four-way intersection, where each road has three lanes leading into the intersection: A right lane for right turns only, a middle lane for going straight only, and a left lane for turning left only. In addition, a single lane is used on each of the four roads for carrying traffic out of the intersection. This simplistic model of an intersection gives us the necessary conditions for testing our model on a four-way intersection.














