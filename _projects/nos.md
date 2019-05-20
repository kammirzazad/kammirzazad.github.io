---
title: Network-Level Design of Cyber-Physical Networks-of-Systems

description: |
  The broad vision of this project is to establish an integrated, comprehensive network-of-system (NoS) design environment as outlined in the figure on the left. At any level, a requirement for systematic design is the definition of a corresponding methodology that breaks the design flow into a necessary and sufficient sequence of steps. Formally, in each step, synthesis is a process of successive exploration and refinement that transforms a specification into an implementation under a set of constraints and optimization objectives.

background: |
  <p> The broad vision of this project is to establish an integrated, comprehensive network-of-system (NoS) design environment as outlined in the figure on the left. At any level, a requirement for systematic design is the definition of a corresponding methodology that breaks the design flow into a necessary and sufficient sequence of steps. Formally, in each step, synthesis is a process of successive exploration and refinement that transforms a specification into an implementation under a set of constraints and optimization objectives. </p>
  <p> This project investigates novel systematic and ultimately automated design approaches that enable network-wide optimization and validation of embedded and cyber-physical systems (CPS) across computation and communication boundaries. A key aspect of CPS and the Internet of Things (IoT) is networking of hitherto disconnected computer systems. However, the networked aspect also poses new design challenges. Machine-to-machine communication comes with inherent uncertainties, such as data losses, yet systems have to perform under tight real-time, reliability, safety, efficiency and performance guarantees. Furthermore, mapping, scheduling and offloading of computations across the network comes with non-obvious tradeoffs that will greatly influence overall application performance and energy consumption. Consequently, on‐ and off‐chip system architectures will have to be designed and optimized taking their role in the overall network environment into account. Likewise, networks have to be assembled considering what systems will be connected as well as the applications running on top of them. Key decisions, such as where and when to execute a certain piece of computation in the network, how many and what types of cores, processors, accelerators, radios and network interfaces each device should have, or the amount of bandwidth and number of access points to be provided by the network cannot be sufficiently answered with current methods that design devices and networks in isolation. When combined with rapidly growing increases in complexity, traditional approaches in which computation and communication aspects are designed separately, and in an ad-hoc manner, hinder achieving system-wide correctness and leave a large optimization potential untapped. Rather, new tools for systematic network/system co‐design are needed. </p>

overview: 
  image: /img/nos/overview.png
  text: |
     <p> The broad vision of this project is to establish an integrated, comprehensive network-of-system (NoS) design environment as outlined in the figure on the left. At any level, a requirement for systematic design is the definition of a corresponding methodology that breaks the design flow into a necessary and sufficient sequence of steps. Formally, in each step, synthesis is a process of successive exploration and refinement that transforms a specification into an implementation under a set of constraints and optimization objectives. </p>
     <p> We first investigate formal models of computation and communication (MoCC) for NoS specification, including associated analysis and synthesis algorithms. We propose Reactive and Adaptive Dataflow Graph (RADF) to clearly and unambiguously define desired NoS behavior. NoS applications written in our programming model are further feed into a compiler and runtime framework (RIoT) to automatically derive optimized implementations with guaranteed correct execution schedule. Finally, we develop a novel NoS simulator (NoSSim) for fast yet accurate network/system co-simulation, where the network/system architecture definition, application mapping, and middleware and runtime system configuration can be optimized with a automatic design space exploration framework. Results of applying our NoS design flow to a range of NoS and IoT application case studies in both simulation and on physical testbeds have shown that it is possible to automatically generate NoS implementations from high-level, abstract application descriptions with real-time and correctness guarantees while maximizing their performance and minimizing resource or energy cost. </p>

outcomes:
  - title: RADF
    image: /img/nos/radf.jpg
    text: | 
       (Reactive and Adaptive Dataflow Graph): Traditional dataflow models have shown their usefulness in analyzing isolated systems. However, these models cannot express the inherent requirements of connected applications, such as dynamic behavior associated with network losses and reactivity to external events. RADF, in addition to traditional lossless channels, provides lossy channels that do not require communication to be reliable. Losses in these channels are represented by replacing lost token(s) with empty token(s). This simple extension allows preserving analyzability and determinism of the underlying data flow model even in the presence of unreliable communication.
    publications:
      - title: |
           S. Francis, A. Gerstlauer, "A Reactive and Adaptive Data Flow Model For Network-of-System Specification," in IEEE Embedded System Letters (ESL), vol. 9, no. 4, pp. 121-124, December 2017.
        pdf: "https://ieeexplore.ieee.org/document/7976277"    
        poster: "https://slam-lab.github.io/NoS/docs/nossim_poster.pdf"

  - title: RIoT
    image: /img/nos/RIoT.png
    text: |
       Given the trade-off between latency and quality in open public networks, deploying distributed streaming applications under latency constraints is not trivial. To enable scheduling of distributed real-time streaming applications, we are developing a quality model for RADF, along with a scheduler that statically derives the optimal link latency budgets given the quality model and latency constraints. Futhermore, to realize the derived schedule and dynamically detect/inject empty tokens, we are proposing a runtime system.

  - title: DeepThings
    image: /img/nos/deepthings.png
    text: |
       A lightweight, general middleware for automatically and adaptively distributing application tasks across heterogeneous NoS clusters to optimize runtime performance while minimizing overheard in the presence of dynamically changing application scenarios. We have specifically applied our approach to execution of deep learning inference applications on resource-constrained IoT edge clusters that would otherwise not be able to run such complex machine learning workloads directly. Using our exploration flow, we were able to derive new task partitioning, mapping and execution strategies that enable running such applications in a distributed fashion with 68% reduced memory requirements and 2x improved speedup compared to existing approaches. 
    publications:
       - title: |
            Z. Zhao, K. Mirzazad Barijough and A. Gerstlauer, "DeepThings: Distributed Adaptive Deep Learning Inference on Resource-Constrained IoT Edge Clusters," CODES+ISSS, special issue of IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), 2018.
         pdf: "https://ieeexplore.ieee.org/document/8493499"
         slides: "https://slam-lab.github.io/NoS/docs/deepthings_slides.ppt"
         poster: "https://slam-lab.github.io/NoS/docs/deepthings_poster.pdf"
         code: "https://github.com/zoranzhao/DeepThings"

  - title: NosSim
    image: /img/nos/nossim.png
    text: |
       A novel NoS simulator for network/system co-simulation and virtual prototyping of NoS architectures and applications. NoSSim makes use of source-level simulation techniques proposed in our previous works to enable fast and accurate full-system simulation. It is further integrated with a exploration framework for rapid, and early design space exploration to support fully automated, joint network/system architecture definition, application mapping, and middleware and runtime system configuration on top of our NoS simulator.
    publications:
       - title: |
            Z. Zhao, V. Tsoutsouras, D. Soudris and A. Gerstlauer, "Network/System Co-Simulation for Design Space Exploration of IoT Applications," in Proceedings of the International Conference on Embedded Computer Systems: Architectures, Modeling and Simulation (SAMOS), 2017.
         pdf: "https://ieeexplore.ieee.org/document/8344610"
         slides: "https://slam-lab.github.io/NoS/docs/nossim_slides.ppt"
         poster: "https://slam-lab.github.io/NoS/docs/nossim_poster.pdf"
         code: "https://github.com/zoranzhao/NoSSim"
       - title: |
            Z. Zhao, A. Gerstlauer and L. K. John, "Source-Level Performance, Energy, Reliability, Power and Thermal (PERPT) Simulation," in IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), 2017.
         pdf: "https://ieeexplore.ieee.org/document/7488221/"
         slides: "https://slam-lab.github.io/NoS/docs/rba_slides.ppt"
         poster: "https://slam-lab.github.io/NoS/docs/rba_tcad_poster.pdf"

publications:
  - title: |
       Zhuoran Zhao, Kamyar Mirzazad Barijough and Andreas Gerstlauer, "DeepThings: Distributed Adaptive Deep Learning Inference on Resource-Constrained IoT Edge Clusters," in IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), Special Issue on Embedded Systems Week (ESWEEK) 2018, International Conference on Hardware/Software Codesign and System Synthesis (CODES+ISSS), vol. 37, no. 11, pp. 2348-2359, October 2018.
    link: "https://ieeexplore.ieee.org/document/8493499"
 
  - title: |
       Sabine Francis, Andreas Gerstlauer, "A Reactive and Adaptive Data Flow Model For Network-of-System Specification," in IEEE Embedded System Letters (ESL), vol. 9, no. 4, pp. 121-124, December 2017.
    link: "https://ieeexplore.ieee.org/document/7976277"

  - title: |
       Zhuoran Zhao, Vasileios Tsoutsouras, Dimitrios Soudris and Andreas Gerstlauer, "Network/System Co-Simulation for Design Space Exploration of IoT Applications," in Proceedings of the International Conference on Embedded Computer Systems: Architectures, Modeling and Simulation (SAMOS), Samos, Greece, July 2017. 
    link: "https://ieeexplore.ieee.org/document/8344610"

  - title: |
       Zhuoran Zhao, Andreas Gerstlauer and Lizy K. John, "Source-Level Performance, Energy, Reliability, Power and Thermal (PERPT) Simulation," in IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), vol. 36, no. 2, pp. 299-312, February 2017.
    link: "https://ieeexplore.ieee.org/document/7488221/"

  - title: |
       Daniel Mueller-Gritschneder, Andreas Gerstlauer, "Host-Compiled Simulation," in Handbook of Hardware/Software Codesign, edited by Soonhoi Ha, Jürgen Teich, Springer, ISBN 978-94-017-7358-4, 2017.
    link: "http://dx.doi.org/10.1007/978-94-017-7358-4_18-1"

  - title: |
       Vania Joloboff, Andreas Gerstlauer, "Virtual Prototyping of Embedded Systems: Speed and Accuracy Tradeoffs," in Cyber-Physical System Design from an Architecture Analysis Viewpoint, Communications of NII Shonan Meetings, edited by Shin Nakajima, Jean-Pierre Talpin, Masumi Toyoshima, Huafeng Yu, Springer, ISBN 978-981-10-4435-9, 2017.
    link: "http://dx.doi.org/10.1007/978-981-10-4436-6_1"

releases:
  - title: "DeepThings"
    link: "https://github.com/SLAM-Lab/DeepThings"
  - title: "NoSSim"
    link: "https://github.com/SLAM-Lab/NoSSim"

funding: 
  - name: "National Science Foundation (NSF) Grant CSR-142164"
    image: /img/icons/NSF_logo.png
    link: "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1421642&HistoricalAwards=false"

people:
  - grad-a
  - grad-d
  - alum-master-c

layout: project
last-updated: 2019-05-06
---
