
# Intrusion Detection System(IDS) on Edge with MEC API 




## Background

Multi-access Edge Computing (MEC) enables the edge network capabilities for application developers – defined by ETSI.The potential threats related to MEC are abuse of assets, compromised supply chain, DoS attacks and physical security.IDS is a critical cybersecurity tool in today’s rapidly evolving cyberthreats landscape and it is becoming more advanced with adoption on cutting edge Deep Learning (DL) technologies on finding near real time issues.This is an important tool to address the threats related to MEC security.Hence it was proposed to create MEC IDS that was submitted and accepted to MEC Hackathon 2022.










## Intrusion Detection System (IDS)

IDS is a security service that monitors and analyzes network traffic for the purpose of finding and providing real-time or near real-time warning of attempts to access system resources in an unauthorized manner.It monitors the edge traffic from the Edge cluster in the Kubernetes solution and filter some of the packets based on the rule and monitor them for anomalies.It works on any Kubernetes platform hence it is not coupled tightly to a particular platform.It triggers an alarm or notification to the Kubernetes platform through the MEC Analytics API to take necessary action.Users who subscribes for these events would get proper warnings/notifications 

## Why an IDS System?

Containers allow all network traffic on the same host by default, which can result in unintentional exposure of data to the wrong containers and  applications do not detect attacks, but instead try their best to fulfill the attackers’ requests.

Advantages:

-   IDS can detect Advanced Persistent Threats (APT)

-   IT can control Unrestricted Traffic and Unsafe Communication

-   If the intrusion is detected quickly enough, the intruder can be identified and ejected easily from the system and less amount of damage

-   An IDS would prevent any Kubernetes platform from the attacks and take necessary actions based on the attack techniques

-   DL methods can automate attack detection, advancing IDS and enabling defenders to act faster and improving the accuracy

## IDS Block Diagram

![image](https://user-images.githubusercontent.com/71922896/204537002-7c173680-ebf4-4861-bae4-a69512842bd4.png)

  
The mirrored network traffic from the Kubernetes platform is sent to IDS. IDS autonomously filters the traffic, analyzes it and then sends alerts to Kubernetes platform. Container Networking Interface (CNI) collects all the ingress traffic to the K8S (Kubernetes) platform by mirroring the traffic (note: the traffic from IDS is not sent to Kubernetes platform). IDS events of whether it is an attack packet, or a normal packet detail will be sent to Kubernetes platform where the MEC Analytics API resource events will be fed. A Pub/sub mechanism (publish/subscribe messaging—also known as pub/sub messaging—is a type of asynchronous service-to-service communication. Any message sent to a subject is immediately read by all the topic's subscribers in a pub/sub paradigm.) based on REST APIs is implemented in which the MEC Analytics API can subscribe for these notifications based on user without burden or overload. 

IDS does a deep packet inspection for Malicious/Suspicious IP packets, specific signature patterns get dropped and is not allowed to the Kubernetes platform. The application captures the mirrored traffic and sends it to the MEC Analytics API which filters the malicious packets at a higher level.



## IDS Deep Learning Model

IDS Model is based on Deep Learning Convolutional Neural Network which is widely called CNN.It analyses the traffic from Kubernetes platform. There are two used classifications – binomial and multiclass.In this work multiclass classification with attack types ‘DoS’ and ‘Probing’ is used.In Network Traffic dataset  , it was analyzed, and 11 features were selected for the classification relevant to the attack types of DoS and Probing.For e.g., the feature “source bytes” and “percentage of packets with errors” can determine the attack as Denial of service.


## MEC Analytics API 

MEC Analytics API supports the following functions:

-   Capture events(attack) from IDS

-   Subscribe mechanism using REST APIs

-   Alerts to the Kubernetes platform

Future Extensions will cover the following scenarios:

-   User can modify subscriptions according to his need

-   MEC API will do the inferencing as the IDS

-   So subsequent methods will be added in MEC API
 


## Deployment 

- IDS with MEC API is deployed in the Intel Dev Cloud platform

-   IDS application is built on the OpenShift sandbox cluster and runs as a pod

-   MEC API application is built on the OpenShift sandbox cluster and runs as a pod

-   Both the pods communicate as a service in the cluster 

-   MEC API Pod runs in the cluster listening on port 5000 and subscribes to IDS pod for specific users

-   IDS Pod listens on that port posting information when there is an attack packet detected

-   MEC API Pod receives the attack information of the particular user and sends notification to the Dev cloud to take necessary actions

## Conclusion and Future Enhancements

-   IDS (Intrusion detection system) is a critical cybersecurity tool in today’s rapidly evolving cyberthreats landscape 

-   This work is focused on to build the MEC API based IDS that will use Deep Learning (DL) methods to automate attack detection

-   IDS detects two attack types of  “DoS”  and “Probing” and notifies MEC API about the attack

-   The IDS model gives an accuracy of 88% and F1 score of 0.9 for the prediction against the actual results.

-   IDS will be further enhanced to detect more attack types 

-   MEC API will be further enhanced to include methods like updation/modification of user details 
