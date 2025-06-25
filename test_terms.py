#!/Users/alexstev/Documents/CiscoDevNet/code/wod/venv/bin/python3
import random
from tinydb import TinyDB, Query

# Database connection
db = TinyDB("db-test.json")
User = Query()


def return_word():
    word_list = [
        {
            "name": "Supervised Learning",
            "definition": "A type of machine learning where a model is trained on labeled data, meaning that each training example is paired with an output label.",
            "url": "https://en.wikipedia.org/wiki/Supervised_learning",
            "id": 0,
        },
        {
            "name": "Unsupervised Learning",
            "definition": "A type of machine learning where a model is trained on unlabeled data and must find patterns and relationships within the data on its own.",
            "url": "https://en.wikipedia.org/wiki/Unsupervised_learning",
            "id": 1,
        },
        {
            "name": "Reinforcement Learning",
            "definition": "A type of machine learning where an agent learns to make decisions by performing actions and receiving rewards or penalties based on those actions.",
            "url": "https://en.wikipedia.org/wiki/Reinforcement_learning",
            "id": 2,
        },
        {
            "name": "Neural Network",
            "definition": "A series of algorithms that attempt to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.",
            "url": "https://en.wikipedia.org/wiki/Artificial_neural_network",
            "id": 3,
        },
        {
            "name": "Deep Learning",
            "definition": "A subset of machine learning that uses algorithms based on neural networks with many layers (deep networks) to model complex patterns in data.",
            "url": "https://en.wikipedia.org/wiki/Deep_learning",
            "id": 4,
        },
        {
            "name": "Natural Language Processing",
            "definition": "A field of artificial intelligence that focuses on the interaction between computers and humans through natural language.",
            "url": "https://en.wikipedia.org/wiki/Natural_language_processing",
            "id": 5,
        },
        {
            "name": "Feature Engineering",
            "definition": "The process of using domain knowledge to extract features (attributes, variables) from raw data to improve the performance of machine learning models.",
            "url": "https://en.wikipedia.org/wiki/Feature_engineering",
            "id": 6,
        },
        {
            "name": "Overfitting",
            "definition": "A modeling error that occurs when a machine learning model learns the training data too well, capturing noise and details that do not generalize to new data.",
            "url": "https://en.wikipedia.org/wiki/Overfitting",
            "id": 7,
        },
        {
            "name": "Underfitting",
            "definition": "A modeling error that occurs when a machine learning model is too simple to capture the underlying patterns in the data.",
            "url": "https://en.wikipedia.org/wiki/Underfitting",
            "id": 8,
        },
        {
            "name": "Cross-Validation",
            "definition": "A technique for assessing how the results of a statistical analysis will generalize to an independent data set, used to prevent overfitting.",
            "url": "https://en.wikipedia.org/wiki/Cross-validation_(statistics)",
            "id": 9,
        },
        {
            "name": "Gradient Descent",
            "definition": "An optimization algorithm used to minimize the loss function in machine learning models by iteratively moving towards the steepest descent of the loss function.",
            "url": "https://en.wikipedia.org/wiki/Gradient_descent",
            "id": 10,
        },
        {
            "name": "Support Vector Machine",
            "definition": "A supervised learning model that finds the hyperplane that best separates different classes in a dataset.",
            "url": "https://en.wikipedia.org/wiki/Support_vector_machine",
            "id": 11,
        },
        {
            "name": "Decision Tree",
            "definition": "A supervised learning model that makes decisions based on a series of binary choices, often visualized as a tree-like diagram.",
            "url": "https://en.wikipedia.org/wiki/Decision_tree_learning",
            "id": 12,
        },
        {
            "name": "Random Forest",
            "definition": "An ensemble learning method that combines multiple decision trees to improve classification or regression accuracy.",
            "url": "https://en.wikipedia.org/wiki/Random_forest",
            "id": 13,
        },
        {
            "name": "K-Nearest Neighbors",
            "definition": "A simple algorithm that classifies a data point based on how its neighbors are classified, typically used for classification and regression.",
            "url": "https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm",
            "id": 14,
        },
        {
            "name": "Dimensionality Reduction",
            "definition": "The process of reducing the number of features (dimensions) in a dataset while preserving its important characteristics.",
            "url": "https://en.wikipedia.org/wiki/Dimensionality_reduction",
            "id": 15,
        },
        {
            "name": "Clustering",
            "definition": "A type of unsupervised learning that groups similar data points into clusters based on their features.",
            "url": "https://en.wikipedia.org/wiki/Cluster_analysis",
            "id": 16,
        },
        {
            "name": "Principal Component Analysis",
            "definition": "A dimensionality reduction technique that transforms data into a set of orthogonal (uncorrelated) components, capturing the most variance in the data.",
            "url": "https://en.wikipedia.org/wiki/Principal_component_analysis",
            "id": 17,
        },
        {
            "name": "Hyperparameter Tuning",
            "definition": "The process of finding the best set of hyperparameters for a machine learning model to optimize its performance.",
            "url": "https://en.wikipedia.org/wiki/Hyperparameter_optimization",
            "id": 18,
        },
        {
            "name": "Ensemble Learning",
            "definition": "A technique that combines predictions from multiple models to improve accuracy and robustness.",
            "url": "https://en.wikipedia.org/wiki/Ensemble_learning",
            "id": 19,
        },
        {
            "name": "Bagging",
            "definition": "A machine learning ensemble method that improves the stability and accuracy of algorithms by training multiple models on different subsets of the data and combining their predictions.",
            "url": "https://en.wikipedia.org/wiki/Bootstrap_aggregating",
            "id": 20,
        },
        {
            "name": "Boosting",
            "definition": "An ensemble learning technique that combines multiple weak learners to create a strong learner by iteratively correcting the errors of the weak models.",
            "url": "https://en.wikipedia.org/wiki/Boosting_(machine_learning)",
            "id": 21,
        },
        {
            "name": "AdaBoost",
            "definition": "A specific type of boosting algorithm that adjusts the weights of incorrectly classified instances to improve the performance of the model.",
            "url": "https://en.wikipedia.org/wiki/AdaBoost",
            "id": 22,
        },
        {
            "name": "Gradient Boosting",
            "definition": "An ensemble technique that builds models sequentially, each new model trying to correct errors made by the previous ones, using gradient descent to minimize errors.",
            "url": "https://en.wikipedia.org/wiki/Gradient_boosting",
            "id": 23,
        },
        {
            "name": "Convolutional Neural Network",
            "definition": "A deep learning algorithm specifically designed for processing structured grid data like images, using convolutional layers to automatically and adaptively learn spatial hierarchies of features.",
            "url": "https://en.wikipedia.org/wiki/Convolutional_neural_network",
            "id": 24,
        },
        {
            "name": "Recurrent Neural Network",
            "definition": "A type of neural network where connections between nodes form directed cycles, allowing the network to maintain a memory of previous inputs, useful for sequence prediction tasks.",
            "url": "https://en.wikipedia.org/wiki/Recurrent_neural_network",
            "id": 25,
        },
        {
            "name": "Long Short-Term Memory",
            "definition": "A special kind of recurrent neural network architecture designed to better retain long-term dependencies by using gates to control the flow of information.",
            "url": "https://en.wikipedia.org/wiki/Long_short-term_memory",
            "id": 26,
        },
        {
            "name": "Autoencoder",
            "definition": "A type of neural network used to learn efficient codings of input data, typically for dimensionality reduction or feature learning.",
            "url": "https://en.wikipedia.org/wiki/Autoencoder",
            "id": 27,
        },
        {
            "name": "Transfer Learning",
            "definition": "A technique in machine learning where a model developed for a particular task is reused as the starting point for a model on a different but related task.",
            "url": "https://en.wikipedia.org/wiki/Transfer_learning",
            "id": 28,
        },
        {
            "name": "Bayesian Network",
            "definition": "A graphical model that represents the probabilistic relationships among a set of variables using directed acyclic graphs.",
            "url": "https://en.wikipedia.org/wiki/Bayesian_network",
            "id": 29,
        },
        {
            "name": "Markov Chain",
            "definition": "A stochastic model that describes a sequence of possible events where the probability of each event depends only on the state attained in the previous event.",
            "url": "https://en.wikipedia.org/wiki/Markov_chain",
            "id": 30,
        },
        {
            "name": "Hidden Markov Model",
            "definition": "A statistical model where the system being modeled is assumed to be a Markov process with unobserved (hidden) states, commonly used in temporal pattern recognition.",
            "url": "https://en.wikipedia.org/wiki/Hidden_Markov_model",
            "id": 31,
        },
        {
            "name": "Q-Learning",
            "definition": "A model-free reinforcement learning algorithm that seeks to learn the value of an action in a particular state in order to maximize the total reward.",
            "url": "https://en.wikipedia.org/wiki/Q-learning",
            "id": 32,
        },
        {
            "name": "Generative Adversarial Network",
            "definition": "A class of machine learning frameworks where two neural networks, a generator and a discriminator, compete against each other to generate realistic data.",
            "url": "https://en.wikipedia.org/wiki/Generative_adversarial_network",
            "id": 33,
        },
        {
            "name": "Hyperparameter",
            "definition": "A parameter whose value is set before the learning process begins and governs the training process, such as learning rate or number of epochs.",
            "url": "https://en.wikipedia.org/wiki/Hyperparameter_optimization",
            "id": 34,
        },
        {
            "name": "Epoch",
            "definition": "One complete pass through the entire training dataset during the training process of a machine learning model.",
            "url": "https://en.wikipedia.org/wiki/Epoch_(machine_learning)",
            "id": 35,
        },
        {
            "name": "Activation Function",
            "definition": "A mathematical function applied to a neural network's node to introduce non-linearity, helping the network learn complex patterns.",
            "url": "https://en.wikipedia.org/wiki/Activation_function",
            "id": 36,
        },
        {
            "name": "Softmax",
            "definition": "An activation function often used in the output layer of a neural network to produce a probability distribution over multiple classes.",
            "url": "https://en.wikipedia.org/wiki/Softmax_function",
            "id": 37,
        },
        {
            "name": "Loss Function",
            "definition": "A function that measures the difference between the predicted output and the actual output during training, guiding the optimization process.",
            "url": "https://en.wikipedia.org/wiki/Loss_function",
            "id": 38,
        },
        {
            "name": "Stochastic Gradient Descent",
            "definition": "An optimization method that reduces the loss by updating the model's parameters using only a small, random subset of the training data.",
            "url": "https://en.wikipedia.org/wiki/Stochastic_gradient_descent",
            "id": 39,
        },
        {
            "name": "Feature engineering",
            "definition": "Feature engineering is a preprocessing step in supervised machine learning and statistical modeling which transforms raw data into a more effective set of inputs. Each input comprises several attributes, known as features. By providing models with relevant information, feature engineering significantly enhances their predictive accuracy and decision-making capability.",
            "url": "https://en.wikipedia.org/wiki/Feature_engineering",
            "id": 40,
        },
        {
            "name": "Hyperparameter optimization",
            "definition": "In machine learning, hyperparameter optimization or tuning is the problem of choosing a set of optimal hyperparameters for a learning algorithm. A hyperparameter is a parameter whose value is used to control the learning process.\n\nHyperparameter optimization determines the set of hyperparameters that yields an optimal model which minimizes a predefined loss function on a given data set. The objective function takes a set of hyperparameters and returns the associated loss. Cross-validation is often used to estimate this generalization performance, and therefore choose the set of values for hyperparameters that maximize it.",
            "url": "https://en.wikipedia.org/wiki/Hyperparameter_optimization",
            "id": 41,
        },
        {
            "name": "Feature extraction vs. Feature selection",
            "definition": "Feature extraction transforms the original features in a dataset into a new set of features, often reducing dimensionality and capturing the most important information. This process can involve techniques like Principal Component Analysis (PCA), which combines features into fewer, more informative ones.\n\nFeature selection involves choosing a subset of the most relevant features from the original dataset without altering them. The goal is to reduce the feature space by eliminating irrelevant or redundant features, which can enhance model performance and reduce overfitting.\n\nIn essence, feature extraction creates new features by transforming data, while feature selection narrows down the features to the most important ones, both aiming to improve the efficiency and accuracy of machine learning models.",
            "url": "https://www.geeksforgeeks.org/difference-between-feature-selection-and-feature-extraction/",
            "id": 42,
        },
        {
            "name": "Transformer",
            "definition": "A transformer is a deep learning architecture developed by researchers at Google and based on the multi-head attention mechanism, proposed in a 2017 paper ‘Attention Is All You Need’. Text is converted to numerical representations called tokens, and each token is converted into a vector via looking up from a word embedding table. At each layer, each token is then contextualized within the scope of the context window with other (unmasked) tokens via a parallel multi-head attention mechanism allowing the signal for key tokens to be amplified and less important tokens to be diminished.\n\nTransformers have the advantage of having no recurrent units, and therefore require less training time than earlier recurrent neural architectures (RNNs) such as long short-term memory (LSTM). Later variations have been widely adopted for training large language models (LLM) on large (language) datasets, such as the Wikipedia corpus and Common Crawl.\n\nTransformers were first developed as an improvement over previous architectures for machine translation, but have found many applications since then. They are used in large-scale natural language processing, computer vision (vision transformers), reinforcement learning, audio, multi-modal processing, robotics, and even playing chess. It has also led to the development of pre-trained systems, such as generative pre-trained transformers (GPTs) and BERT (Bidirectional Encoder Representations from Transformers).",
            "url": "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)",
            "id": 43,
        },
        {
            "name": "Feedforward neural network (FNN)",
            "definition": "A feedforward neural network (FNN) is one of the two broad types of artificial neural network, characterized by direction of the flow of information between its layers. Its flow is uni-directional, meaning that the information in the model flows in only one direction—forward—from the input nodes, through the hidden nodes (if any) and to the output nodes, without any cycles or loops, in contrast to recurrent neural networks, which have a bi-directional flow. Modern feedforward networks are trained using the backpropagation method and are colloquially referred to as the ‘vanilla’ neural networks.",
            "url": "https://en.wikipedia.org/wiki/Feedforward_neural_network",
            "id": 44,
        },
        {
            "name": "Named-entity recognition (NER)",
            "definition": "Named-entity recognition (NER) (also known as (named) entity identification, entity chunking, and entity extraction) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.",
            "url": "https://en.wikipedia.org/wiki/Named-entity_recognition",
            "id": 45,
        },
        {
            "name": "Machine learning (ML)",
            "definition": "Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so. Machine learning algorithms are used in a wide variety of applications, such as in medicine, email filtering, speech recognition, and computer vision, where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks.\n\nA subset of machine learning is closely related to computational statistics, which focuses on making predictions using computers; but not all machine learning is statistical learning. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. \n\nData mining is a related field of study, focusing on exploratory data analysis through unsupervised learning. Some implementations of machine learning use data and neural networks in a way that mimics the working of a biological brain. In its application across business problems, machine learning is also referred to as predictive analytics.",
            "url": "https://en.wikipedia.org/wiki/Machine_learning",
            "id": 46,
        },
        {
            "name": "Artificial empathy (AE)",
            "definition": "Artificial empathy (AE) or computational empathy is the development of AI systems—such as companion robots or virtual agents—that can detect emotions and respond to them in an empathic way.\n\nAlthough such technology can be perceived as scary or threatening, it could also have a significant advantage over humans for roles in which emotional expression can be important, such as in the health care sector. For example, care-givers who perform emotional labor above and beyond the requirements of paid labor can experience chronic stress or burnout, and can become desensitized to patients.\n\nA broader definition of artificial empathy is ‘the ability of nonhuman models to predict a person's internal state (e.g., cognitive, affective, physical) given the signals (s)he emits (e.g., facial expression, voice, gesture) or to predict a person's reaction (including, but not limited to internal states) when he or she is exposed to a given set of stimuli (e.g., facial expression, voice, gesture, graphics, music, etc.)’.",
            "url": "https://en.wikipedia.org/wiki/Artificial_empathy",
            "id": 47,
        },
        {
            "name": "Onboard intelligence",
            "definition": "The capability of a device to solve a problem itself without passing the request to another computer in the network. Onboard intelligence also refers to artificial intelligence that's built into a device design, rather than outsourced to remote technology.",
            "url": "https://www.techopedia.com/definition/33391/onboard-intelligence",
            "id": 48,
        },
        {
            "name": "AI winter",
            "definition": "In the history of artificial intelligence, an AI winter is a period of reduced funding and interest in artificial intelligence research. The term was coined by analogy to the idea of a nuclear winter. The field has experienced several hype cycles, followed by disappointment and criticism, followed by funding cuts, followed by renewed interest years or decades later.\n\nEnthusiasm and optimism about AI has generally increased since its low point in the early 1990s. Beginning about 2012, interest in artificial intelligence (and especially the sub-field of machine learning) from the research and corporate communities led to a dramatic increase in funding and investment.",
            "url": "https://en.wikipedia.org/wiki/AI_winter",
            "id": 49,
        },
        {
            "name": "Expert system",
            "definition": "In artificial intelligence, an expert system is a computer system emulating the decision-making ability of a human expert. Expert systems are designed to solve complex problems by reasoning through bodies of knowledge, represented mainly as if–then rules rather than through conventional procedural code. The first expert systems were created in the 1970s and then proliferated in the 1980s. Expert systems were among the first truly successful forms of artificial intelligence (AI) software. \n\nAn expert system is divided into two subsystems: the inference engine and the knowledge base. The knowledge base represents facts and rules. The inference engine applies the rules to the known facts to deduce new facts. Inference engines can also include explanation and debugging abilities.",
            "url": "https://en.wikipedia.org/wiki/Expert_system",
            "id": 50,
        },
        {
            "name": "John McCarthy",
            "definition": "John McCarthy (September 4, 1927 – October 24, 2011) was an American computer scientist and cognitive scientist. He was one of the founders of the discipline of artificial intelligence. He co-authored the document that coined the term ‘artificial intelligence’ (AI), developed the programming language family Lisp, significantly influenced the design of the language ALGOL, popularized time-sharing, and invented garbage collection.\n\nSeveral Key Theme’s in McCarthy’s Work\n\n- The idea that the world can be represented symbolically for a machine and reasoned about by that machine.\n- The division of the AI problem into two parts: epistemological (representation) and heuristic (search).\n- The importance of formal (mathematical) representation, particularly the use of logic for representation.\n- The use of reification—the conceptual turning of abstract structures (such as situations) into concrete instances that can be reasoned about. The situation calculus, where the state of the universe is compressed into a single constant, is an example of such reification.\n- The development of abstract and general mechanisms (proof checkers, logic, circumscription, common sense) in contrast with domain-specific tools and languages.\n- The relatively complete analysis of artificial domains (programming languages, puzzles, chess) instead of a (necessarily) incomplete analysis of natural situations.\n- The importance of environments for interactive exploration. This is illustrated not so much by an explicit campaign position of McCarthy's as by the systems whose creation he led, such as the AI lab, Lisp, and timesharing.\n\nAwards and honors\n\n- Turing Award from the Association for Computing Machinery (1971)\n- Kyoto Prize (1988)\n- National Medal of Science (USA) in Mathematical, Statistical, and Computational Sciences (1990)\n- Inducted as a Fellow of the Computer History Museum ‘for his co-founding of the fields of Artificial Intelligence (AI) and timesharing systems, and for major contributions to mathematics and computer science’. (1999)\n- Benjamin Franklin Medal in Computer and Cognitive Science from the Franklin Institute (2003)\n- Inducted into IEEE Intelligent Systems' AI's Hall of Fame (2011), for the ‘significant contributions to the field of AI and intelligent systems’.",
            "url": "https://en.wikipedia.org/wiki/John_McCarthy_(computer_scientist)",
            "id": 51,
        },
        {
            "name": "Artificial general intelligence (AGI)",
            "definition": "Artificial general intelligence (AGI) is the ability of an intelligent agent to understand or learn any intellectual task that a human being can. It is a primary goal of some artificial intelligence research and a common topic in science fiction and futures studies. AGI can also be referred to as strong AI, full AI, or general intelligent action, although some academic sources reserve the term ‘strong AI’ for computer programs that experience sentience or consciousness.\n\nIn contrast to strong AI, weak AI or ‘narrow AI’ is not intended to have general cognitive abilities; rather, weak AI is any program that is designed to solve exactly one problem. (Academic sources reserve ‘weak AI’ for programs that do not experience consciousness or do not have a mind in the same sense people do.) A 2020 survey identified 72 active AGI R&D projects spread across 37 countries.",
            "url": "https://en.wikipedia.org/wiki/Artificial_general_intelligence",
            "id": 52,
        },
        {
            "name": "Superintelligence",
            "definition": "A superintelligence is a hypothetical agent that possesses intelligence far surpassing that of the brightest and most gifted human minds. ‘Superintelligence’ may also refer to a property of problem-solving systems (e.g., superintelligent language translators or engineering assistants) whether or not these high-level intellectual competencies are embodied in agents that act in the world. A superintelligence may or may not be created by an intelligence explosion and associated with a technological singularity. University of Oxford philosopher Nick Bostrom defines superintelligence as ‘any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest’. \n\nTechnological researchers disagree about how likely present-day human intelligence is to be surpassed. Some argue that advances in artificial intelligence (AI) will probably result in general reasoning systems that lack human cognitive limitations. Others believe that humans will evolve or directly modify their biology so as to achieve radically greater intelligence. A number of futures studies scenarios combine elements from both of these possibilities, suggesting that humans are likely to interface with computers, or upload their minds to computers, in a way that enables substantial intelligence amplification.\n\nSome researchers believe that superintelligence will likely follow shortly after the development of artificial general intelligence. The first generally intelligent machines are likely to immediately hold an enormous advantage in at least some forms of mental capability, including the capacity of perfect recall, a vastly superior knowledge base, and the ability to multitask in ways not possible to biological entities. This may give them the opportunity to—either as a single being or as a new species—become much more powerful than humans, and to displace them.\n\nA number of scientists and forecasters argue for prioritizing early research into the possible benefits and risks of human and machine cognitive enhancement, because of the potential social impact of such technologies in both raising the level of collective human intelligence and in intelligently ushering the age of super intelligence as a whole.",
            "url": "https://en.wikipedia.org/wiki/Superintelligence",
            "id": 53,
        },
        {
            "name": "Human Level Machine Intelligence (HLMI)",
            "definition": "Human-Level Machine Intelligence (HLMI), also known as Human-Level Artificial intelligence, refers to computer systems that can operate with the intelligence of an average human being. These programs can complete tasks or make decisions as successfully as the average human can.",
            "url": "https://arxiv.org/abs/2108.03793",
            "id": 54,
        },
        {
            "name": "Seed AI",
            "definition": "Seed AI is a hypothesized type of strong artificial intelligence capable of recursive self-improvement. Having improved itself it would become better at improving itself, potentially leading to an exponential increase in intelligence. No such AI currently exists, but researchers are working to make seed AI a reality.\n\nModern compilers optimize for efficiency and raw speed, but this is not sufficient for the sort of open-ended recursive self-enhancement needed to create superintelligence, as a true seed AI would need to be able to do. Existing optimizers can transform code into a functionally equivalent, more efficient form, but cannot identify the intent of an algorithm and rewrite it for more effective results. The optimized version of a given compiler may compile faster, but it cannot compile better. That is, an optimized version of a compiler will never spot new optimization tricks that earlier versions failed to see or innovate new ways of improving its own program. Seed AI must be able to understand the purpose behind the various elements of its design, and design entirely new modules that will make it genuinely more intelligent and more effective in fulfilling its purpose.\n\nCreating seed AI is the goal of several organizations. The Singularity Institute for Artificial Intelligence is the most prominent of those explicitly working to create seed AI. Others include the Artificial General Intelligence Research Institute, creator of the Novamente AI engine, and Adaptive Artificial Intelligence Incorporated.",
            "url": "https://towardsdatascience.com/seed-ai-history-philosophy-and-state-of-the-art-22b5294b21b5",
            "id": 55,
        },
        {
            "name": "Orthogonality thesis",
            "definition": "The Orthogonality Thesis states that an agent can have any combination of intelligence level and final goal, that is, its Utility Functions and General Intelligence can vary independently of each other. This is in contrast to the belief that, because of their intelligence, AIs will all converge to a common goal.",
            "url": "https://en.wikipedia.org/wiki/Existential_risk_from_artificial_general_intelligence#Orthogonality_thesis",
            "id": 56,
        },
        {
            "name": "Liquid Neural Network",
            "definition": "Liquid neural networks are a class of artificial intelligence systems that learn on the job, even after their training. In other words, they utilize ‘liquid’ algorithms that continuously adapt to new information, such as a new environment, just like the brains of living organisms.\n\nRecent research has demonstrated the efficiency of a new kind of very small—20,000 parameter—machine-learning system called a liquid neural network. They showed that drones equipped with these excelled in navigating complex, new environments with precision, even edging out state-of-the art systems. The systems were able to make decisions that led them to a target in previously unexplored forests and city spaces, and they could do it in the presence of added noise and other difficulties.",
            "url": "https://spectrum.ieee.org/liquid-neural-networks",
            "id": 57,
        },
        {
            "name": "AI alignment",
            "definition": "In the field of artificial intelligence (AI), AI alignment research aims to steer AI systems towards humans' intended goals, preferences, or ethical principles. An AI system is considered aligned if it advances the intended objectives. A misaligned AI system pursues some objectives, but not the intended ones.",
            "url": "https://en.wikipedia.org/wiki/AI_alignment",
            "id": 58,
        },
        {
            "name": "AIOps",
            "definition": "AIOps is artificial intelligence for IT operations. It refers to the strategic use of AI, machine learning (ML), and machine reasoning (MR) technologies throughout IT operations to simplify and streamline processes and optimize the use of IT resources.",
            "url": "https://www.cisco.com/c/en/us/solutions/artificial-intelligence/what-is-aiops.html",
            "id": 59,
        },
        {
            "name": "Indirect normativity",
            "definition": "Indirect normativity is an approach to the AI alignment problem that attempts to specify AI values indirectly, such as by reference to what a rational agent would value under idealized conditions, rather than via direct specification. It is a method of control by which the motivation of the superintelligence is shaped not directly, but indirectly. The approach specifies a process for the superintelligence to determine beneficial goals rather than specifying them directly.",
            "url": "https://ordinaryideas.wordpress.com/2012/04/21/indirect-normativity-write-up/",
            "id": 60,
        },
        {
            "name": "Data bias vs. Algorithmic bias vs. Evaluation bias",
            "definition": "Data bias occurs when the training data used for a model is unrepresentative or imbalanced, leading to skewed outcomes that reflect those biases.\n\nAlgorithmic bias arises when the design or mechanics of an algorithm inherently favor certain outcomes, independent of the data, often due to flawed assumptions or incorrect model implementations.\n\nEvaluation bias happens when the metrics or methods used to assess a model’s performance do not adequately capture its fairness or accuracy across different groups, resulting in misleading conclusions about its effectiveness or equity. Each type of bias can impact AI models in unique ways, but they all contribute to unfair or inaccurate decision-making if not properly addressed.\n\nOther types of biases found in AI are discussed in the article linked below.",
            "url": "https://www.ibm.com/topics/ai-bias",
            "id": 61,
        },
        {
            "name": "Context window",
            "definition": "A context window refers to the amount of text or information an AI model can consider at one time when generating a response or making a prediction. It defines the range of input tokens (words or characters) the model can 'see' and use to understand the current context. For example, if a model has a context window of 2048 tokens, it can process and generate responses based on up to 2048 tokens of input text at once. Anything beyond this limit is typically truncated or ignored, which can affect the model's understanding and coherence in longer conversations or documents.",
            "url": "https://www.respell.ai/post/what-are-context-windows-and-what-do-they-do",
            "id": 62,
        },
        {
            "name": "Data wrangling",
            "definition": "Data wrangling, sometimes referred to as data munging, is the process of transforming and mapping data from one ‘raw’ data form into another format with the intent of making it more appropriate and valuable for a variety of downstream purposes such as analytics. The goal of data wrangling is to assure quality and useful data. Data analysts typically spend the majority of their time in the process of data wrangling compared to the actual analysis of the data.",
            "url": "https://en.wikipedia.org/wiki/Data_wrangling",
            "id": 63,
        },
        {
            "name": "Prediction vs. Forecasting",
            "definition": "Prediction in AI refers to estimating the outcome or value of a specific event or data point based on current or historical data, often without considering the element of time. It typically deals with classification or regression tasks, such as predicting whether an email is spam or estimating house prices.\n\nForecasting, on the other hand, specifically involves making estimates about future events by analyzing trends, patterns, and historical data over time. It accounts for temporal dynamics and is commonly used for time series analysis, such as forecasting stock prices or weather conditions. While both involve estimating outcomes, forecasting is inherently temporal, focusing on future trends, whereas prediction is more general and can apply to both present and future data points.",
            "url": "https://plat.ai/blog/difference-between-prediction-and-forecast/",
            "id": 64,
        },
        {
            "name": "Explainable AI (XAI)",
            "definition": "Explainable AI (XAI) refers to a set of methods and techniques designed to make the outputs and decision-making processes of AI models more understandable and interpretable to humans. The goal of XAI is to provide transparency in AI systems, enabling users to comprehend how and why a model makes specific predictions or decisions. This is crucial for building trust, ensuring accountability, and identifying potential biases or errors in the model.\n\nXAI techniques can include visualizations, feature importance scores, or simplified models that approximate complex ones. It is especially important in high-stakes fields like healthcare, finance, and legal systems, where understanding the rationale behind AI decisions is essential for ethical and responsible use.",
            "url": "https://en.wikipedia.org/wiki/Explainable_artificial_intelligence",
            "id": 65,
        },
        {
            "name": "Multi-agent system",
            "definition": "A multi-agent system (MAS or ‘self-organized system’) is a computerized system composed of multiple interacting intelligent agents. Multi-agent systems can solve problems that are difficult or impossible for an individual agent or a monolithic system to solve. Intelligence may include methodic, functional, procedural approaches, algorithmic search or reinforcement learning.",
            "url": "https://en.wikipedia.org/wiki/Multi-agent_system",
            "id": 66,
        },
        {
            "name": "Information theory",
            "definition": "Information theory is the mathematical study of the quantification, storage, and communication of information. The field was established and put on a firm footing by Claude Shannon in the 1940s, though early contributions were made in the 1920s through the works of Harry Nyquist and Ralph Hartley. It is at the intersection of electronic engineering, mathematics, statistics, computer science, neurobiology, physics, and electrical engineering.\n\nA key measure in information theory is entropy. Entropy quantifies the amount of uncertainty involved in the value of a random variable or the outcome of a random process. For example, identifying the outcome of a fair coin flip (which has two equally likely outcomes) provides less information (lower entropy, less uncertainty) than identifying the outcome from a roll of a die (which has six equally likely outcomes). Some other important measures in information theory are mutual information, channel capacity, error exponents, and relative entropy. Important sub-fields of information theory include source coding, algorithmic complexity theory, algorithmic information theory and information-theoretic security.",
            "url": "https://en.wikipedia.org/wiki/Information_theory",
            "id": 67,
        },
        {
            "name": "Graphical model",
            "definition": "A graphical model or probabilistic graphical model (PGM) or structured probabilistic model is a probabilistic model for which a graph expresses the conditional dependence structure between random variables. They are commonly used in probability theory, statistics—particularly Bayesian statistics—and machine learning.\n\nGenerally, probabilistic graphical models use a graph-based representation as the foundation for encoding a distribution over a multi-dimensional space and a graph that is a compact or factorized representation of a set of independences that hold in the specific distribution.\n\nTwo branches of graphical representations of distributions are commonly used, namely, Bayesian networks and Markov random fields. Both families encompass the properties of factorization and independences, but they differ in the set of independences they can encode and the factorization of the distribution that they induce.",
            "url": "https://en.wikipedia.org/wiki/Graphical_model",
            "id": 68,
        },
        {
            "name": "Markov Decision Process",
            "definition": "Markov decision process (MDP), also called a stochastic dynamic program or stochastic control problem, is a model for sequential decision making when outcomes are uncertain.\n\nOriginating from operations research in the 1950s, MDPs have since gained recognition in a variety of fields, including ecology, economics, healthcare, telecommunications and reinforcement learning. Reinforcement learning utilizes the MDP framework to model the interaction between a learning agent and its environment. In this framework, the interaction is characterized by states, actions, and rewards. The MDP framework is designed to provide a simplified representation of key elements of artificial intelligence challenges. These elements encompass the understanding of cause and effect, the management of uncertainty and nondeterminism, and the pursuit of explicit goals.\n\nThe name comes from its connection to Markov chains, a concept developed by the Russian mathematician Andrey Markov. The ‘Markov’ in ‘Markov decision process’ refers to the underlying structure of state transitions that still follow the Markov property. The process is called a ‘decision process’ because it involves making decisions that influence these state transitions, extending the concept of a Markov chain into the realm of decision-making under uncertainty.",
            "url": "https://en.wikipedia.org/wiki/Markov_decision_process",
            "id": 69,
        },
        {
            "name": "Exploration-exploitation tradeoff",
            "definition": "The exploration-exploitation dilemma, also known as the explore-exploit tradeoff, is a fundamental concept in decision-making that arises in many domains. It is depicted as the balancing act between two opposing strategies. Exploitation involves choosing the best option based on current knowledge of the system (which may be incomplete or misleading), while exploration involves trying out new options that may lead to better outcomes in the future at the expense of an exploitation opportunity. Finding the optimal balance between these two strategies is a crucial challenge in many decision-making problems whose goal is to maximize long-term benefits.\n\nIn the context of machine learning, the exploration-exploitation tradeoff is fundamental in reinforcement learning (RL), a type of machine learning that involves training agents to make decisions based on feedback from the environment. Crucially, this feedback may be incomplete or delayed. The agent must decide whether to exploit the current best-known policy or explore new policies to improve its performance.",
            "url": "https://en.wikipedia.org/wiki/Exploration-exploitation_dilemma",
            "id": 70,
        },
        {
            "name": "AI Washing",
            "definition": "AI washing is a deceptive marketing tactic that consists of promoting a product or a service by overstating the role of artificial intelligence integration in it. It raises concerns regarding transparency, consumer trust in the AI industry, and compliance with security regulations, potentially hampering legitimate advancements in AI.",
            "url": "https://en.wikipedia.org/wiki/AI_washing",
            "id": 71,
        },
        {
            "name": "seq2seq",
            "definition": "seq2seq is a family of machine learning approaches used for natural language processing. Applications include language translation, image captioning, conversational models, and text summarization. Seq2seq uses sequence transformation: it turns one sequence into another sequence.\n\nConcretely, seq2seq maps an input sequence into a real-numerical vector by a neural network (the encoder), then map it back to an output sequence using another neural network (the decoder).",
            "url": "https://en.wikipedia.org/wiki/Seq2seq",
            "id": 72,
        },
        {
            "name": "Encoder–Decoder Architecture",
            "definition": "Encoder-decoder architectures are powerful tools used in machine learning, specifically for tasks involving sequences like text or speech. They consist of two parts: an encoder that takes a variable-length sequence as input, and a decoder that acts as a conditional language model The encoder takes a variable-length sequence as input and transforms it into a state with a fixed shape. The decoder maps the vector representation back to a variable-length target sequence.",
            "url": "https://d2l.ai/chapter_recurrent-modern/encoder-decoder.html",
            "id": 73,
        },
        {
            "name": "Siamese neural network",
            "definition": "A Siamese neural network (sometimes called a twin neural network) is an artificial neural network that uses the same weights while working in tandem on two different input vectors to compute comparable output vectors. Often one of the output vectors is precomputed, thus forming a baseline against which the other output vector is compared. This is similar to comparing fingerprints but can be described more technically as a distance function for locality-sensitive hashing.\n\nUses of similarity measures where a twin network might be used are such things as recognizing handwritten checks, automatic detection of faces in camera images, and matching queries with indexed documents.\n\nThe perhaps most well-known application of twin networks are face recognition, where known images of people are precomputed and compared to an image from a turnstile or similar. It is not obvious at first, but there are two slightly different problems. One is recognizing a person among a large number of other persons, that is the facial recognition problem. DeepFace is an example of such a system. In its most extreme form this is recognizing a single person at a train station or airport. The other is face verification, that is to verify whether the photo in a pass is the same as the person claiming he or she is the same person. The twin network might be the same, but the implementation can be quite different.",
            "url": "https://en.wikipedia.org/wiki/Siamese_neural_network",
            "id": 74,
        },
        {
            "name": "Central Limit Theorem",
            "definition": "The Central Limit Theorem (CLT) states that the distribution of the sum (or average) of a large number of independent and identically distributed random variables tends to be normally distributed, regardless of the original distribution of the variables. This theorem is foundational in statistics because it justifies the use of the normal distribution in many statistical methods and helps in making inferences about population parameters based on sample statistics.\n\n(CLT) states that, under appropriate conditions, the distribution of a normalized version of the sample mean converges to a standard normal distribution. This holds even if the original variables themselves are not normally distributed. There are several versions of the CLT, each applying in the context of different conditions.",
            "url": "https://en.wikipedia.org/wiki/Central_limit_theorem",
            "id": 75,
        },
        {
            "name": "Backpropagation",
            "definition": "Backpropagation is a supervised learning algorithm used for training artificial neural networks. It involves a forward pass where input data is processed through the network to produce an output, followed by a backward pass where the algorithm calculates the gradient of the loss function with respect to each weight by the chain rule. This information is then used to update the weights to minimize the error in predictions. Backpropagation is essential for the efficient training of deep learning models.",
            "url": "https://en.wikipedia.org/wiki/Backpropagation",
            "id": 76,
        },
        {
            "name": "Ground Value vs. Output Value",
            "definition": "In the context of machine learning and neural networks, the ground value (or ground truth) refers to the actual, known value or label for a particular input sample, representing the expected outcome. The output value is the predicted value produced by the model after processing the input. Evaluating the difference between the ground value and the output value is crucial for measuring the model's performance and calculating the loss during training.",
            "url": "https://en.wikipedia.org/wiki/Ground_truth",
            "id": 77,
        },
        {
            "name": "Local vs. Global Maxima and Minima",
            "definition": "In optimization, a local maximum is a point where the function value is higher than all nearby points, while a global maximum is the highest point in the entire function. Similarly, a local minimum is lower than its neighbors, while a global minimum is the lowest point overall. Distinguishing between local and global extrema is important, especially in complex functions where optimization algorithms may get stuck in local optima.",
            "url": "https://en.wikipedia.org/wiki/Maximum_and_minimum",
            "id": 78,
        },
        {
            "name": "Convex Optimization",
            "definition": "Convex optimization is a subfield of mathematical optimization that studies the problem of minimizing convex functions over convex sets. A function is convex if its second derivative is positive, indicating that the curve bends upwards, while a set is convex if, for any two points within the set, the line segment connecting them lies entirely within the set. Convex optimization problems have desirable properties, such as having a unique global minimum, making them easier to solve.",
            "url": "https://en.wikipedia.org/wiki/Convex_optimization",
            "id": 79,
        },
        {
            "name": "Robot Learning",
            "definition": "Robot learning is a field of study focused on the ability of robots to learn from their environments and experiences to improve their performance on tasks. It encompasses various techniques from machine learning and artificial intelligence, allowing robots to adapt to changes, learn new skills, and make decisions autonomously. Robot learning combines elements of reinforcement learning, supervised learning, and unsupervised learning to enable robots to operate effectively in dynamic settings.",
            "url": "https://en.wikipedia.org/wiki/Robot_learning",
            "id": 80,
        },
        {
            "name": "One-shot learning",
            "definition": "One-shot learning is an object categorization problem, found mostly in computer vision. Whereas most machine learning-based object categorization algorithms require training on hundreds or thousands of examples, one-shot learning aims to classify objects from one, or only a few, examples. The term few-shot learning is also used for these problems, especially when more than one example is needed.",
            "url": "https://en.wikipedia.org/wiki/One-shot_learning_(computer_vision)",
            "id": 81,
        },
        {
            "name": "Zero-shot learning",
            "definition": "Zero-shot learning (ZSL) is a problem setup in deep learning where, at test time, a learner observes samples from classes which were not observed during training, and needs to predict the class that they belong to. The name is a play on words based on the earlier concept of one-shot learning, in which classification can be learned from only one, or a few, examples.\n\nZero-shot methods generally work by associating observed and non-observed classes through some form of auxiliary information, which encodes observable distinguishing properties of objects. For example, given a set of images of animals to be classified, along with auxiliary textual descriptions of what animals look like, an artificial intelligence model which has been trained to recognize horses, but has never been given a zebra, can still recognize a zebra when it also knows that zebras look like striped horses. This problem is widely studied in computer vision, natural language processing, and machine perception.",
            "url": "https://en.wikipedia.org/wiki/Zero-shot_learning",
            "id": 82,
        },
        {
            "name": "Graph neural network",
            "definition": "A graph neural network (GNN) belongs to a class of artificial neural networks for processing data that can be represented as graphs.\n\nIn the more general subject of ‘geometric deep learning’, certain existing neural network architectures can be interpreted as GNNs operating on suitably defined graphs. A convolutional neural network layer, in the context of computer vision, can be considered a GNN applied to graphs whose nodes are pixels and only adjacent pixels are connected by edges in the graph. A transformer layer, in natural language processing, can be considered a GNN applied to complete graphs whose nodes are words or tokens in a passage of natural language text.",
            "url": "https://en.wikipedia.org/wiki/Graph_neural_network",
            "id": 83,
        },
        {
            "name": "Deep reinforcement learning",
            "definition": "Deep reinforcement learning (deep RL) is a subfield of machine learning that combines reinforcement learning (RL) and deep learning. RL considers the problem of a computational agent learning to make decisions by trial and error. Deep RL incorporates deep learning into the solution, allowing agents to make decisions from unstructured input data without manual engineering of the state space.\n\nDeep RL algorithms are able to take in very large inputs (e.g. every pixel rendered to the screen in a video game) and decide what actions to perform to optimize an objective (e.g. maximizing the game score). Deep reinforcement learning has been used for a diverse set of applications including but not limited to robotics, video games, natural language processing, computer vision, education, transportation, finance and healthcare.",
            "url": "https://en.wikipedia.org/wiki/Deep_reinforcement_learning",
            "id": 84,
        },
        {
            "name": "Data-Centric AI",
            "definition": "Data-Centric AI (DCAI) is an emerging science that studies techniques to improve datasets, which is often the best way to improve performance in practical ML applications. While good data scientists have long practiced this manually via ad hoc trial/error and intuition, DCAI considers the improvement of data as a systematic engineering discipline.\n\nWhile manual exploratory data analysis is a key first step of understanding and improving any dataset, data-centric AI uses AI methods to more systematically diagnose and fix issues that commonly plague real-world datasets. Data-centric AI can take one of two forms:\n\n- AI algorithms that understand data and use that information to improve models. Curriculum learning is an example of this, in which ML models are trained on ‘easy data’ first.\n\n- AI algorithms that modify data to improve AI models. Confident learning is an example of this, in which ML models are trained on a filtered dataset where mislabeled data has been removed.\n\nIn both examples above, determining which data is easy or mislabeled is estimated automatically via algorithms applied to the outputs of trained ML models.",
            "url": "https://dcai.csail.mit.edu/",
            "id": 85,
        },
        {
            "name": "Exponential smoothing",
            "definition": "Exponential smoothing or exponential moving average (EMA) is a rule of thumb technique for smoothing time series data using the exponential window function. Whereas in the simple moving average the past observations are weighted equally, exponential functions are used to assign exponentially decreasing weights over time.\n\nIt is an easily learned and easily applied procedure for making some determination based on prior assumptions by the user, such as seasonality. Exponential smoothing is often used for analysis of time-series data.",
            "url": "https://en.wikipedia.org/wiki/Exponential_smoothing",
            "id": 86
        },
        {
            "name": "ARIMA",
            "definition": "In time series analysis used in statistics and econometrics, autoregressive integrated moving average (ARIMA) and seasonal ARIMA (SARIMA) models are generalizations of the autoregressive moving average (ARMA) model to non-stationary series and periodic variation, respectively. All these models are fitted to time series in order to better understand it and predict future values. The purpose of these generalizations is to fit the data as well as possible. Specifically, ARMA assumes that the series is stationary, that is, its expected value is constant in time. If instead the series has a trend (but a constant variance/autocovariance), the trend is removed by ‘differencing’, leaving a stationary series. This operation generalizes ARMA and corresponds to the ‘integrated’ part of ARIMA. Analogously, periodic variation is removed by ‘seasonal differencing’.",
            "url": "https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average",
            "id": 87
        },
        {
            "name": "Seasonality",
            "definition": "In time series data, seasonality refers to the trends that occur at specific regular intervals less than a year, such as weekly, monthly, or quarterly. Seasonality may be caused by various factors, such as weather, vacation, and holidays and consists of periodic, repetitive, and generally regular and predictable patterns in the levels of a time series.\n\nSeasonal fluctuations in a time series can be contrasted with cyclical patterns. The latter occur when the data exhibits rises and falls that are not of a fixed period. Such non-seasonal fluctuations are usually due to economic conditions and are often related to the ‘business cycle’; their period usually extends beyond a single year, and the fluctuations are usually of at least two years.",
            "url": "https://en.wikipedia.org/wiki/Seasonality",
            "id": 88
        },
        {
            "name": "Pearson Correlation",
            "definition": "In statistics, the Pearson correlation coefficient (PCC) is a correlation coefficient that measures linear correlation between two sets of data. It is the ratio between the covariance of two variables and the product of their standard deviations; thus, it is essentially a normalized measurement of the covariance, such that the result always has a value between −1 and 1. As with covariance itself, the measure can only reflect a linear correlation of variables, and ignores many other types of relationships or correlations. As a simple example, one would expect the age and height of a sample of children from a primary school to have a Pearson correlation coefficient significantly greater than 0, but less than 1 (as 1 would represent an unrealistically perfect correlation).",
            "url": "https://en.wikipedia.org/wiki/Pearson_correlation_coefficient",
            "id": 89
        },
        {
            "name": "Concept drift",
            "definition": "In predictive analytics, data science, machine learning and related fields, concept drift or drift is an evolution of data that invalidates the data model. It happens when the statistical properties of the target variable, which the model is trying to predict, change over time in unforeseen ways. This causes problems because the predictions become less accurate as time passes. Drift detection and drift adaptation are of paramount importance in the fields that involve dynamically changing data and data models.",
            "url": "https://en.wikipedia.org/wiki/Concept_drift",
            "id": 90
        },
        {
            "name": "Curriculum learning",
            "definition": "Curriculum learning is a technique in machine learning in which a model is trained on examples of increasing difficulty, where the definition of ‘difficulty’ may be provided externally or discovered automatically as part of the training process. This is intended to attain good performance more quickly, or to converge to a better local optimum if the global optimum is not found.",
            "url": "https://en.wikipedia.org/wiki/Curriculum_learning",
            "id": 91
        },
        {
            "name": "Confident learning",
            "definition": "Confident learning (CL) is an alternative approach to machine learning. It focuses on label quality by characterizing and identifying label errors in datasets. The approach is based on the principles of pruning noisy data, counting with probabilistic thresholds to estimate noise, and ranking examples to train with confidence",
            "url": "https://arxiv.org/abs/1911.00068",
            "id": 92
        },
        {
            "name": "Weak supervision",
            "definition": "Weak supervision (also known as semi-supervised learning) is a paradigm in machine learning, the relevance and notability of which increased with the advent of large language models due to large amount of data required to train them. It is characterized by using a combination of a small amount of human-labeled data (exclusively used in more expensive and time-consuming supervised learning paradigm), followed by a large amount of unlabeled data (used exclusively in unsupervised learning paradigm).\n\nIn other words, the desired output values are provided only for a subset of the training data. The remaining data is unlabeled or imprecisely labeled. Intuitively, it can be seen as an exam and labeled data as sample problems that the teacher solves for the class as an aid in solving another set of problems. In the transductive setting, these unsolved problems act as exam questions. In the inductive setting, they become practice problems of the sort that will make up the exam. Technically, it could be viewed as performing clustering and then labeling the clusters with the labeled data, pushing the decision boundary away from high-density regions, or learning an underlying one-dimensional manifold where the data reside.",
            "url": "https://en.wikipedia.org/wiki/Weak_supervision",
            "id": 93
        },
        {
            "name": "Local Interpretable Model-Agnostic Explanations (Lime)",
            "definition": "LIME (Local Interpretable Model-Agnostic Explanations) is a technique used in machine learning to explain the predictions made by complex, black-box models such as neural networks, ensemble methods (e.g., random forests, gradient boosting), or other algorithms that are not easily interpretable. It provides a way to understand why a model made a specific prediction for a given input.\n\nLIME is also a Python library which can be installed via pip (pip install lime) or by cloning the repository and installing it (git clone https://github.com/marcotcr/lime.git).LIME supports explanations for text classifiers, tabular data, and image classifiers.",
            "url": "https://arxiv.org/abs/1602.04938",
            "id": 94
        },
        {
            "name": "Auditability in ML",
            "definition": "Auditability in the AI context refers to the preparedness of an AI system to assess its algorithms, models, data, and design processes. Such assessment of AI applications by internal and external auditors helps justify the trustworthiness of the AI system. AI auditing is a necessary practice that exhibits the responsibility of AI system design and the justifiability of predictions delivered by models. AI auditability covers:\n- Evaluation of models, algorithms, and data streams\n- Analysis of operations, results, and anomalies observed\n- Technical aspects of AI systems for results accuracy\n- Ethical aspects of AI systems for fairness, legality, and privacy.\n\nAuditing AI systems is a modern approach to educate the C-suite about the value of AI adoptions, expose the risks involved to the businesses, and develop safeguard controls to avoid threats detected in audits. AI auditing defines systematic and piloted programs for better risk assessment and a high level of governance.\n\nEffective AI auditing requires the involvement of internal teams and third-party auditors. Enterprises sometimes need to share sensitive information to understand AI-driven functions that must be aligned with regulatory requirements or industry practices. It is recommended to keep a comprehensive record of data procurement, provenance, preprocessing, storage and lineage. Further, it includes reports on data availability, the integrity of data sources, data relevance, security aspects, and unforeseen data issues across data pipelines.",
            "url": "https://censius.ai/blogs/ai-audit-guide",
            "id": 95
        },
        {
            "name": "Knowledge distillation",
            "definition": "In machine learning, knowledge distillation or model distillation is the process of transferring knowledge from a large model to a smaller one. While large models (such as very deep neural networks or ensembles of many models) have more knowledge capacity than small models, this capacity might not be fully utilized. It can be just as computationally expensive to evaluate a model even if it utilizes little of its knowledge capacity. Knowledge distillation transfers knowledge from a large model to a smaller one without loss of validity. As smaller models are less expensive to evaluate, they can be deployed on less powerful hardware (such as a mobile device).",
            "url": "https://en.wikipedia.org/wiki/Knowledge_distillation",
            "id": 96
        },
        {
            "name": "Model compression",
            "definition": "Model compression is a machine learning technique for reducing the size of trained models. Large models can achieve high accuracy, but often at the cost of significant resource requirements. Compression techniques aim to compress models without significant performance reduction. Smaller models require less storage space, and consume less memory and compute during inference.\n\nCompressed models enable deployment on resource-constrained devices such as smartphones, embedded systems, edge computing devices, and consumer electronics computers. Efficient inference is also valuable for large corporations that serve large model inference over an API, allowing them to reduce computational costs and improve response times for users.\n\nModel compression is not to be confused with knowledge distillation, in which a separate, smaller ‘student’ model is trained to imitate the input-output behavior of a larger ‘teacher’ model.",
            "url": "https://en.wikipedia.org/wiki/Model_compression",
            "id": 97
        },
        {
            "name": "Perceptron",
            "definition": "In machine learning, the perceptron (or McCulloch-Pitts neuron) is an algorithm for supervised learning of binary classifiers. A binary classifier is a function which can decide whether or not an input, represented by a vector of numbers, belongs to some specific class. It is a type of linear classifier, i.e. a classification algorithm that makes its predictions based on a linear predictor function combining a set of weights with the feature vector.",
            "url": "https://en.wikipedia.org/wiki/Perceptron",
            "id": 98
        },
        {
            "name": "AutoML-Zero",
            "definition": "AutoML-Zero is an approach developed by researchers at Google Research aimed at pushing the boundaries of automated machine learning (AutoML). Traditional AutoML focuses on automating the process of model selection, hyperparameter tuning, and training. AutoML-Zero takes this a step further by attempting to automatically discover machine learning algorithms from scratch, starting with only basic mathematical operations.",
            "url": "https://research.google/blog/automl-zero-evolving-code-that-learns/",
            "id": 99
        },
        {
            "name": "Automated machine learning (AutoML)",
            "definition": "Automated machine learning (AutoML) is the process of automating the tasks of applying machine learning to real-world problems. It is the combination of automation and ML.\n\nAutoML potentially includes every stage from beginning with a raw dataset to building a machine learning model ready for deployment. AutoML was proposed as an artificial intelligence-based solution to the growing challenge of applying machine learning. The high degree of automation in AutoML aims to allow non-experts to make use of machine learning models and techniques without requiring them to become experts in machine learning. Automating the process of applying machine learning end-to-end additionally offers the advantages of producing simpler solutions, faster creation of those solutions, and models that often outperform hand-designed models.\n\nCommon techniques used in AutoML include hyperparameter optimization, meta-learning and neural architecture search.",
            "url": "https://en.wikipedia.org/wiki/Automated_machine_learning",
            "id": 100
        },
        {
            "name": "Naïve Bayes",
            "definition": "Naïve Bayes is a family of probabilistic algorithms based on applying Bayes' theorem with the assumption of conditional independence between features. It is commonly used in text classification and spam filtering tasks.",
            "url": "https://en.wikipedia.org/wiki/Naive_Bayes_classifier",
            "id": 101
        },
        {
            "name": "Logistic Regression",
            "definition": "Logistic Regression is a statistical method for analyzing a dataset in which one or more independent variables determine an outcome that is categorical, such as binary classification problems. It uses the logistic function to model probabilities.",
            "url": "https://en.wikipedia.org/wiki/Logistic_regression",
            "id": 102
        },
        {
            "name": "HuggingFace",
            "definition": "HuggingFace is a company and open-source platform providing tools and libraries for natural language processing (NLP) tasks, including pre-trained transformer models such as BERT, GPT, and others. It simplifies the implementation of state-of-the-art NLP models.",
            "url": "https://huggingface.co/",
            "id": 103
        },
        {
            "name": "Incremental training",
            "definition": "Incremental training is a machine learning approach in which a model is updated and trained further as new data becomes available, without retraining from scratch. It is particularly useful in environments with streaming data or frequent updates.",
            "url": "https://en.wikipedia.org/wiki/Incremental_learning",
            "id": 104
        },
        {
            "name": "One hot encoded",
            "definition": "One hot encoding is a method used to convert categorical data variables into binary vectors. Each category is represented as a unique binary vector, ensuring that no two categories have overlapping representations.",
            "url": "https://en.wikipedia.org/wiki/One-hot",
            "id": 105
        },
        {
            "name": "Bidirectional LSTM",
            "definition": "A Bidirectional Long Short-Term Memory (BiLSTM) network is a type of recurrent neural network (RNN) that processes data in both forward and backward directions. It is commonly used in natural language processing tasks for context-aware predictions.",
            "url": "https://www.sciencedirect.com/topics/computer-science/bidirectional-long-short-term-memory-network",
            "id": 106
        },
        {
            "name": "Softmax activation",
            "definition": "Softmax activation is a function used in neural networks to convert raw model outputs (logits) into probability distributions. It is commonly applied in the output layer for multi-class classification tasks.",
            "url": "https://www.coursera.org/articles/softmax-activation-function",
            "id": 107
        },
        {
            "name": "Feed forward dense network",
            "definition": "A feed forward dense network is a type of artificial neural network in which connections between the nodes do not form a cycle. Data flows in one direction, from input to output, passing through fully connected layers.",
            "url": "https://arxiv.org/abs/2312.10560",
            "id": 108
        },
        {
            "name": "Small language model",
            "definition": "A small language model refers to a natural language processing model that has a relatively smaller number of parameters compared to larger models like GPT-3. These models are more computationally efficient and often used for specific tasks.",
            "url": "https://www.ibm.com/think/topics/small-language-models",
            "id": 109
        },
        {
            "name": "Retrieval Interleaved Generation (RIG)",
            "definition": "Retrieval Interleaved Generation (RIG) is an approach in natural language processing that combines retrieval-based methods with generation techniques. It retrieves relevant content and integrates it into generated outputs for better context.",
            "url": "https://www.llmwatch.com/p/googles-rag-alternative-retrieval",
            "id": 110
        },
        {
            "name": "Exploding Gradients",
            "definition": "Exploding gradients is a problem in training deep neural networks where gradients become very large, causing instability or failure during optimization. Techniques like gradient clipping are used to mitigate this issue.",
            "url": "https://machinelearningmastery.com/exploding-gradients-in-neural-networks/",
            "id": 111
        },
        {
            "name": "Machine Learning Control",
            "definition": "Machine learning control involves the use of machine learning algorithms to design and optimize control systems for dynamic processes. It is often applied in robotics, autonomous systems, and industrial automation.",
            "url": "https://en.wikipedia.org/wiki/Machine_learning_control",
            "id": 112
        },
        {
            "name": "Computer Vision",
            "definition": "Computer vision is a field of artificial intelligence that trains computers to interpret and make decisions based on visual data, such as images or videos. Applications include facial recognition, object detection, and autonomous vehicles.",
            "url": "https://www.ibm.com/topics/computer-vision",
            "id": 113
        },
        {
            "name": "Post Hoc Algorithm",
            "definition": "Post hoc algorithms are techniques applied after an event or process to analyze results and provide interpretability or explanations for model decisions in machine learning.",
            "url": "https://www.sciencedirect.com/science/article/pii/S1389041724000378",
            "id": 114
        },
        {
            "name": "Depth-First Search and Breadth-First Search",
            "definition": "Depth-First Search (DFS) and Breadth-First Search (BFS) are graph traversal algorithms. DFS explores as far as possible along a branch before backtracking, while BFS explores all neighbors at the current depth before moving deeper.",
            "url": "https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/",
            "id": 115
        },
        {
            "name": "Simulated Annealing",
            "definition": "Simulated annealing is an optimization technique inspired by the annealing process in metallurgy. It is used to find a global minimum of a cost function by probabilistically allowing worse solutions in the hope of escaping local minima.",
            "url": "https://en.wikipedia.org/wiki/Simulated_annealing",
            "id": 116
        },
        {
            "name": "Particle Swarm",
            "definition": "Particle swarm optimization (PSO) is a computational method inspired by the social behavior of birds and fish. It is used to optimize problems by iteratively improving candidate solutions with respect to a given measure of quality.",
            "url": "https://en.wikipedia.org/wiki/Particle_swarm_optimization",
            "id": 117
        },
        {
            "name": "Mixture of Experts (MoE)",
            "definition": "Mixture of Experts (MoE) is a machine learning approach that uses a combination of specialized models (experts) and a gating mechanism to decide which expert to use for a specific input.",
            "url": "https://en.wikipedia.org/wiki/Mixture_of_experts",
            "id": 118
        },
        {
            "name": "DBRX",
            "definition": "DBRX is a proprietary or specialized term, often referring to a deep-learning-based exploratory framework for specific domains or datasets. Contextual usage determines its exact application.",
            "url": "https://en.wikipedia.org/wiki/DBRX",
            "id": 119
        },
        {
            "name": "Bayesian Inference",
            "definition": "Bayesian inference is a method of statistical inference that updates the probability of a hypothesis as more evidence or information becomes available, based on Bayes' theorem.",
            "url": "https://en.wikipedia.org/wiki/Bayesian_inference",
            "id": 120
        },
        {
            "name": "Monte Carlo Methods",
            "definition": "Monte Carlo methods are computational algorithms that rely on repeated random sampling to obtain numerical results. They are widely used in optimization, numerical integration, and probabilistic modeling.",
            "url": "https://en.wikipedia.org/wiki/Monte_Carlo_method",
            "id": 121
        },
        {
            "name": "Chain of Thought",
            "definition": "Chain of Thought is a reasoning framework in machine learning that involves generating intermediate reasoning steps to solve complex problems, improving the model's ability to reason systematically.",
            "url": "https://arxiv.org/abs/2201.11903",
            "id": 122
        },
        {
            "name": "Batch, Stochastic, and Mini-batch Gradient Descent",
            "definition": "Batch, stochastic, and mini-batch gradient descent are optimization methods for training machine learning models. They differ in the amount of data used to compute gradients at each step, affecting speed and convergence.",
            "url": "https://machinelearningmastery.com/gentle-introduction-mini-batch-gradient-descent-configure-batch-size/",
            "id": 123
        },
        {
            "name": "Stochastic Methods",
            "definition": "Stochastic methods use randomness as part of their logic to solve problems or optimize functions. They are commonly employed in optimization algorithms and machine learning models.",
            "url": "https://en.wikipedia.org/wiki/Stochastic_process",
            "id": 124
        },
        {
            "name": "Genetic Algorithms",
            "definition": "Genetic algorithms are search heuristics inspired by natural selection principles. They evolve solutions to optimization problems through operations like mutation, crossover, and selection.",
            "url": "https://en.wikipedia.org/wiki/Genetic_algorithm",
            "id": 125
        },
        {
            "name": "Adam",
            "definition": "Adam is an optimization algorithm for training deep learning models. It combines the benefits of Adagrad and RMSprop by using adaptive learning rates and momentum.",
            "url": "https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/",
            "id": 126
        },
        {
            "name": "RMSprop",
            "definition": "RMSprop is an optimization algorithm designed to adapt learning rates for each parameter. It is particularly effective for training deep neural networks and tackling vanishing or exploding gradient issues.",
            "url": "https://towardsdatascience.com/understanding-rmsprop-faster-neural-network-learning-62e116fcf29a",
            "id": 127
        },
        {
            "name": "Convex Optimization",
            "definition": "Convex optimization is a subfield of optimization focused on problems where the objective function is convex and constraints define a convex set. Solutions can be efficiently found using mathematical techniques.",
            "url": "https://en.wikipedia.org/wiki/Convex_optimization",
            "id": 128
        },
        {
            "name": "MCAR, MAR, MNAR",
            "definition": "MCAR (Missing Completely At Random), MAR (Missing At Random), and MNAR (Missing Not At Random) are categories used in statistics and machine learning to describe missing data mechanisms, impacting how data imputation or analysis should be handled.",
            "url": "https://en.wikipedia.org/wiki/Missing_data",
            "id": 129
        },
        {
            "name": "Kernel Density Estimation",
            "definition": "Kernel Density Estimation (KDE) is a non-parametric way to estimate the probability density function of a dataset, useful in statistics, anomaly detection, and visualization of data distributions.",
            "url": "https://en.wikipedia.org/wiki/Kernel_density_estimation",
            "id": 130
        },
        {
            "name": "Agentic",
            "definition": "In AI and cognitive science, agentic refers to systems or entities that exhibit goal-directed behavior, autonomy, and decision-making, such as intelligent agents in reinforcement learning.",
            "url": "https://en.wikipedia.org/wiki/Intelligent_agent",
            "id": 131
        },
        {
            "name": "Lazy Evaluation",
            "definition": "Lazy evaluation is a programming technique where computations are deferred until their results are needed, improving efficiency in functional programming and machine learning pipelines.",
            "url": "https://en.wikipedia.org/wiki/Lazy_evaluation",
            "id": 132
        },
        {
            "name": "Ensemble Approach and Voting Approach",
            "definition": "The ensemble approach combines multiple models to improve predictive performance, with the voting approach being a method where multiple classifiers vote on the final prediction, enhancing robustness.",
            "url": "https://en.wikipedia.org/wiki/Ensemble_learning",
            "id": 133
        },
        {
            "name": "Local Outlier Factor (LOF)",
            "definition": "The Local Outlier Factor (LOF) algorithm detects anomalies by measuring the local density deviation of a data point compared to its neighbors, useful in fraud detection and anomaly detection.",
            "url": "https://en.wikipedia.org/wiki/Local_outlier_factor",
            "id": 134
        },
        {
            "name": "Contamination Parameter",
            "definition": "The contamination parameter in anomaly detection specifies the expected proportion of outliers in the dataset, impacting model sensitivity in methods like LOF and Isolation Forest.",
            "url": "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html",
            "id": 135
        },
        {
            "name": "Isolation Forest",
            "definition": "Isolation Forest is an unsupervised anomaly detection algorithm that isolates anomalies through recursive partitioning, making it efficient for large datasets.",
            "url": "https://en.wikipedia.org/wiki/Isolation_forest",
            "id": 136
        },
        {
            "name": "Decision Stump",
            "definition": "A decision stump is a simple decision tree with only one split, often used as a weak learner in ensemble methods like AdaBoost.",
            "url": "https://en.wikipedia.org/wiki/Decision_stump",
            "id": 137
        },
        {
            "name": "Meta-learning",
            "definition": "Meta-learning, or 'learning to learn,' is a machine learning approach where models improve their learning process based on experience from multiple tasks.",
            "url": "https://en.wikipedia.org/wiki/Meta-learning_(computer_science)",
            "id": 138
        },
        {
            "name": "Stacking",
            "definition": "Stacking is an ensemble learning technique that combines multiple base models using a meta-learner to improve predictive performance.",
            "url": "https://en.wikipedia.org/wiki/Ensemble_learning#Stacking",
            "id": 139
        },
        {
            "name": "LightGBM",
            "definition": "LightGBM is a gradient boosting framework optimized for speed and efficiency, using histogram-based learning to handle large datasets with reduced memory usage.",
            "url": "https://lightgbm.readthedocs.io/en/latest/",
            "id": 140
        },
        {
            "name": "Shrinkage",
            "definition": "Shrinkage is a regularization technique used in gradient boosting to reduce the impact of individual trees, improving generalization and preventing overfitting.",
            "url": "https://en.wikipedia.org/wiki/Shrinkage_(statistics)",
            "id": 141
        },
        {
            "name": "XGBoost",
            "definition": "XGBoost is an optimized gradient boosting framework designed for speed and performance, widely used in machine learning competitions and real-world applications.",
            "url": "https://en.wikipedia.org/wiki/XGBoost",
            "id": 142
        },
        {
            "name": "Weak Learners",
            "definition": "Weak learners, such as decision stumps, are models that perform slightly better than random guessing and are often combined in boosting algorithms to create strong classifiers.",
            "url": "https://en.wikipedia.org/wiki/Weak_learners",
            "id": 143
        },
        {
            "name": "Residual",
            "definition": "In machine learning, a residual is the difference between the observed value and the predicted value, playing a crucial role in gradient boosting and regression models.",
            "url": "https://en.wikipedia.org/wiki/Errors_and_residuals",
            "id": 144
        },
        {
            "name": "Gradient Boosting Machines (GBMs)",
            "definition": "Gradient Boosting Machines (GBMs) are ensemble learning methods that iteratively train weak learners to minimize errors by focusing on the residuals of previous models.",
            "url": "https://en.wikipedia.org/wiki/Gradient_boosting",
            "id": 145
        },
        {
            "name": "Inertia",
            "definition": "Inertia is a measure of clustering quality in k-means, representing the sum of squared distances of samples to their nearest cluster center.",
            "url": "https://scikit-learn.org/stable/modules/clustering.html#k-means",
            "id": 146
        },
        {
            "name": "Silhouette Score",
            "definition": "The silhouette score evaluates clustering performance by measuring how similar a data point is to its own cluster compared to other clusters, with values ranging from -1 to 1.",
            "url": "https://en.wikipedia.org/wiki/Silhouette_(clustering)",
            "id": 147
        },
        {
            "name": "Dendrogram",
            "definition": "A dendrogram is a tree-like diagram that illustrates the arrangement of clusters formed by hierarchical clustering algorithms, depicting the order and distance at which data points are merged.",
            "url": "https://www.geeksforgeeks.org/hierarchical-clustering/",
            "id": 148
        },
        {
            "name": "Auto-regressive Algorithm",
            "definition": "An auto-regressive algorithm is a type of time series model where future values are regressed on their own previous values, capturing temporal dependencies to forecast future points.",
            "url": "https://aws.amazon.com/what-is/autoregressive-models/",
            "id": 149
        },
        {
            "name": "MAE vs. MAPE",
            "definition": "Mean Absolute Error (MAE) measures the average magnitude of errors in a set of predictions, without considering their direction, while Mean Absolute Percentage Error (MAPE) expresses this error as a percentage of the actual values, providing a normalized measure of prediction accuracy.",
            "url": "https://sefidian.com/2022/08/18/a-guide-on-regression-error-metrics-with-python-code/",
            "id": 150
        },
        {
            "name": "Convergence",
            "definition": "In machine learning, convergence refers to the process where an algorithm iteratively adjusts its parameters and approaches a stable state or solution, typically minimizing a loss function over time.",
            "url": "https://mljourney.com/what-is-convergence-in-machine-learning/",
            "id": 151
        },
        {
            "name": "t-SNE",
            "definition": "t-Distributed Stochastic Neighbor Embedding (t-SNE) is a non-linear dimensionality reduction technique used for visualizing high-dimensional data by mapping it into two or three dimensions, preserving local structures and revealing patterns in the data.",
            "url": "https://www.geeksforgeeks.org/ml-t-distributed-stochastic-neighbor-embedding-t-sne-algorithm/",
            "id": 152
        },
        {
            "name": "Chain Rule",
            "definition": "The chain rule is a fundamental property of probability that allows the decomposition of joint probabilities into conditional probabilities. The chain rule allows us to find the derivative of composite functions, which frequently arise in machine learning models due to their layered architecture. These models often involve multiple nested functions, and the chain rule helps us compute gradients efficiently for optimization algorithms like gradient descent.",
            "url": "https://www.geeksforgeeks.org/chain-rule-derivative-in-machine-learning/",
            "id": 153
        },
        {
            "name": "FP-Growth",
            "definition": "FP-Growth is a frequent pattern mining algorithm that efficiently discovers itemsets without candidate generation. An implementation of FP-Growth can be found in MLxtend, a Python library providing various extensions for machine learning.",
            "url": "https://rasbt.github.io/mlxtend/user_guide/frequent_patterns/fpgrowth/",
            "id": 154
        },
        {
            "name": "Bag of Words",
            "definition": "The Bag of Words (BoW) model is a representation used in natural language processing where text data is converted into numerical feature vectors by counting word occurrences, disregarding grammar and word order.",
            "url": "https://machinelearningmastery.com/gentle-introduction-bag-words-model/",
            "id": 155
        },
        {
            "name": "train_test_split()",
            "definition": "train_test_split() is a function in Scikit-learn that splits a dataset into training and testing subsets, commonly used in machine learning to evaluate model performance by training on one portion and validating on another.",
            "url": "https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html",
            "id": 156
        },
        {
            "name": "Cross Validation",
            "definition": "Cross-validation is a statistical technique used to assess the generalization ability of machine learning models by splitting data into multiple training and validation sets, helping to prevent overfitting.",
            "url": "https://www.statology.org/complete-guide-cross-validation/",
            "id": 157
        },
        {
            "name": "Linear Support Vector Classification",
            "definition": "Linear Support Vector Classification (LinearSVC) is a machine learning algorithm that finds the optimal hyperplane to separate data points in a linear manner, often used for classification tasks with high-dimensional datasets.",
            "url": "https://www.datatechnotes.com/2020/07/classification-example-with-linearsvm-in-python.html",
            "id": 158
        },
        {
            "name": "Downsampling vs. Upsampling",
            "definition": "Downsampling and upsampling are techniques used to handle imbalanced datasets. Downsampling involves reducing the number of instances in the majority class, while upsampling involves increasing the number of instances in the minority class to balance the dataset.",
            "url": "https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/",
            "id": 159
        },
        {
            "name": "The ‘Zero Frequency’ Problem",
            "definition": "The 'zero frequency' problem occurs in text classification when a word appears in the test set but not in the training set, leading to a zero probability estimate for that word. This is commonly addressed by smoothing techniques like Laplace smoothing.",
            "url": "https://www.atoti.io/articles/how-to-solve-the-zero-frequency-problem-in-naive-bayes/",
            "id": 160
        },
        {
            "name": "Hard-voting vs. Soft-voting",
            "definition": "Hard-voting involves classifying based on the majority of predictions made by multiple models, while soft-voting uses the predicted probabilities, averaging them to make a final decision. Soft-voting generally performs better when models provide well-calibrated probabilities.",
            "url": "https://vitalflux.com/hard-vs-soft-voting-classifier-python-example/",
            "id": 161
        },
        {
            "name": "Homogeneous vs. Heterogeneous Ensemble Model",
            "definition": "A homogeneous ensemble model consists of multiple instances of the same type of model (e.g., multiple decision trees), while a heterogeneous ensemble model combines different types of models (e.g., decision trees, logistic regression, etc.) to improve performance.",
            "url": "https://onlinelibrary.wiley.com/doi/10.1155/2013/312067?msockid=1058fb0a6ff96e591ff4eeb96e9b6fda",
            "id": 162
        },
        {
            "name": "LightGBM",
            "definition": "LightGBM (Light Gradient Boosting Machine) is an open-source, distributed, high-performance gradient boosting framework that is particularly efficient in terms of both speed and memory usage, designed for large datasets.",
            "url": "https://lightgbm.readthedocs.io/en/latest/",
            "id": 163
        },
        {
            "name": "Model Distillation",
            "definition": "Model distillation is a technique where a smaller, simpler model is trained to mimic the behavior of a larger, more complex model. This is useful for deploying models on resource-constrained devices without compromising performance significantly.",
            "url": "https://arxiv.org/abs/1503.02531",
            "id": 164
        },
        {
            "name": "Stacking",
            "definition": "Stacking is an ensemble learning technique where multiple models (often of different types) are trained to predict the same target, and a meta-model is used to combine their predictions to make a final decision.",
            "url": "https://www.scaler.com/topics/machine-learning/stacking-in-machine-learning/",
            "id": 165
        },
        {
            "name": "K-means++",
            "definition": "K-means++ is an enhancement of the standard K-means algorithm that improves the initialization of cluster centroids. It selects initial centroids in a way that spreads them out, which helps avoid poor clustering results caused by random initialization.",
            "url": "https://en.wikipedia.org/wiki/K-means%2B%2B",
            "id": 166
        },
        {
            "name": "Chi-squared tests",
            "definition": "The Chi-squared test is a statistical method used to determine if there is a significant association between categorical variables, comparing observed frequencies with expected frequencies.",
            "url": "https://www.statisticshowto.com/probability-and-statistics/chi-square/",
            "id": 167
        },
        {
            "name": "ANOVA, ANCOVA, MANOVA, and MANCOVA",
            "definition": "ANOVA (Analysis of Variance) tests for differences between group means, ANCOVA (Analysis of Covariance) combines ANOVA with regression to control for continuous variables. MANOVA (Multivariate Analysis of Variance) extends ANOVA to multiple dependent variables, and MANCOVA adds control for continuous covariates in MANOVA.",
            "url": "https://www.statsmakemecry.com/smmctheblog/stats-soup-anova-ancova-manova-mancova",
            "id": 168
        },
        {
            "name": "Simple Linear Regression vs. Multiple Linear Regression",
            "definition": "Simple linear regression models the relationship between a dependent variable and one independent variable, while multiple linear regression models the relationship between a dependent variable and multiple independent variables.",
            "url": "https://www.investopedia.com/ask/answers/060315/what-difference-between-linear-regression-and-multiple-regression.asp",
            "id": 169
        },
        {
            "name": "Ordinary Least Squares (OLS)",
            "definition": "Ordinary Least Squares (OLS) is a method of estimating the parameters of a linear regression model by minimizing the sum of the squared differences between the observed and predicted values.",
            "url": "https://en.wikipedia.org/wiki/Ordinary_least_squares",
            "id": 170
        },
        {
            "name": "Logistic Regression vs. Linear Regression",
            "definition": "Linear regression is used to predict continuous values, while logistic regression is used to predict categorical outcomes, specifically binary outcomes by modeling the probability of an event occurring.",
            "url": "https://www.geeksforgeeks.org/ml-linear-regression-vs-logistic-regression/",
            "id": 171
        },
        {
            "name": "R-squared and Adjusted R-squared",
            "definition": "R-squared (coefficient of determination) measures how well the independent variables explain the variance in the dependent variable. Adjusted R-squared adjusts R-squared for the number of predictors in the model, providing a more accurate measure when comparing models with different numbers of predictors.",
            "url": "https://www.datacamp.com/tutorial/adjusted-r-squared",
            "id": 172
        },
        {
            "name": "Multiple Linear Regression",
            "definition": "Multiple linear regression is an extension of simple linear regression where multiple independent variables are used to predict a dependent variable.",
            "url": "https://www.scribbr.com/statistics/multiple-linear-regression/",
            "id": 173
        },
        {
            "name": "Forward Selection",
            "definition": "Forward selection is a feature selection technique that starts with no variables in the model and adds them one by one based on the statistical significance of the variables in improving model performance.",
            "url": "https://www.analyticsvidhya.com/blog/2021/04/forward-feature-selection-and-its-implementation/",
            "id": 174
        },
        {
            "name": "Regularization: Lasso, Ridge, and Elastic Net Regression",
            "definition": "Regularization techniques like Lasso, Ridge, and Elastic Net are used in regression models to prevent overfitting by adding penalties to the model's complexity. Lasso uses L1 regularization, Ridge uses L2 regularization, and Elastic Net combines both.",
            "url": "https://www.geeksforgeeks.org/lasso-vs-ridge-vs-elastic-net-ml/",
            "id": 175
        },
        {
            "name": "Backward Elimination",
            "definition": "Backward elimination is a feature selection method that starts with all predictors in the model and removes the least significant variables one at a time until a specified criterion is met.",
            "url": "https://towardsdatascience.com/backward-elimination-for-feature-selection-in-machine-learning-c6a3a8f8cef4/",
            "id": 176
        },
        {
            "name": "Extra-sum-of-squares F-test",
            "definition": "The extra-sum-of-squares F-test is used to compare two nested models by determining if adding additional predictors to the model significantly improves the fit to the data.",
            "url": "https://www.graphpad.com/guides/prism/latest/curve-fitting/reg_interpreting_comparison_of_mod_2.htm",
            "id": 177
        },
        {
            "name": "Elbow Method",
            "definition": "The elbow method is a technique used in clustering to determine the optimal number of clusters by plotting the sum of squared distances (within-cluster variance) and looking for the 'elbow' point where the rate of decrease slows down.",
            "url": "https://en.wikipedia.org/wiki/Elbow_method_(clustering)",
            "id": 178
        },
        {
            "name": "Hierarchical Clustering",
            "definition": "Hierarchical clustering is a clustering technique that builds a hierarchy of clusters by either merging smaller clusters (agglomerative) or splitting larger clusters (divisive). It is useful when the number of clusters is not pre-specified.",
            "url": "https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering",
            "id": 179
        },
        {
            "name": "Permutation Language Modeling",
            "definition": "Permutation language modeling is a training objective used in models like XLNet, where the model predicts tokens based on all possible permutations of the input sequence, capturing bidirectional context without masking.",
            "url": "https://chanys.github.io/plm/",
            "id": 180
        },
        {
            "name": "Autoregressive (AR) Model",
            "definition": "An autoregressive model predicts future values in a time series as a linear function of past observations and a stochastic term, commonly used in econometrics and signal processing.",
            "url": "https://en.wikipedia.org/wiki/Autoregressive_model",
            "id": 181
        },
        {
            "name": "Transformers vs. RNNs for NLP",
            "definition": "Transformers utilize self-attention mechanisms to process entire sequences simultaneously, enabling better parallelization and capturing long-range dependencies, whereas RNNs process sequences sequentially, which can be less efficient and struggle with long-term dependencies.",
            "url": "https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452/",
            "id": 182
        },
        {
            "name": "KVM (Key-Value Memory)",
            "definition": "Key-Value Memory networks store information as key-value pairs, allowing models to retrieve relevant data by matching input queries with stored keys, enhancing tasks like question answering and language modeling.",
            "url": "https://arxiv.org/abs/1606.03126",
            "id": 183
        },
        {
            "name": "RoPE vs. Additive Positional Encoding",
            "definition": "RoPE (Rotary Positional Encoding) encodes positional information through rotations in embedding space, preserving relative positions, while additive positional encoding adds fixed or learned position vectors to token embeddings.",
            "url": "https://arxiv.org/abs/2104.09864",
            "id": 184
        },
        {
            "name": "Self-Attention",
            "definition": "Self-attention allows models to weigh the importance of different words in an input sequence when encoding a particular word, enabling the capture of contextual relationships within the sequence.",
            "url": "https://armanasq.github.io/nlp/self-attention/",
            "id": 185
        },
        {
            "name": "Negative Sampling",
            "definition": "Negative sampling is a technique used in training models like word2vec, where the model learns to distinguish target word-context pairs from randomly sampled negative pairs, improving training efficiency.",
            "url": "https://www.youtube.com/watch?v=4PXILCmVK4Q",
            "id": 186
        },
        {
            "name": "Neural Machine Translation (NMT)",
            "definition": "Neural Machine Translation uses neural networks to model the entire translation process end-to-end, typically employing encoder-decoder architectures with attention mechanisms to translate text from one language to another.",
            "url": "https://en.wikipedia.org/wiki/Neural_machine_translation",
            "id": 187
        },
        {
            "name": "Vision and Language Pre-training (VLP)",
            "definition": "VLP involves training models on combined visual and textual data to learn representations that can be fine-tuned for tasks like image captioning, visual question answering, and multimodal retrieval.",
            "url": "https://arxiv.org/abs/2202.09061",
            "id": 188
        },
        {
            "name": "Opinion Mining",
            "definition": "Opinion mining, or sentiment analysis, is the process of using natural language processing to identify and extract subjective information from text, such as opinions, sentiments, and emotions.",
            "url": "https://en.wikipedia.org/wiki/Sentiment_analysis",
            "id": 189
        },
        {
            "name": "Meta-Learning",
            "definition": "Meta-learning, or 'learning to learn', involves designing models that can adapt quickly to new tasks with minimal data by leveraging knowledge acquired from previous tasks.",
            "url": "https://arxiv.org/abs/2004.05439",
            "id": 190
        },
        {
            "name": "Multimodal Models",
            "definition": "Multimodal models are designed to process and integrate information from multiple modalities, such as text, images, and audio, enabling them to perform tasks that require understanding across different types of data.",
            "url": "https://en.wikipedia.org/wiki/Multimodal_learning",
            "id": 191
        },
        {
            "name": "Attention Mechanisms",
            "definition": "Attention mechanisms allow models to focus on specific parts of the input sequence when generating each part of the output, improving performance in tasks like translation and summarization.",
            "url": "https://www.geeksforgeeks.org/types-of-attention-mechanism/",
            "id": 192
        },
        {
            "name": "Sequence-to-Sequence Models",
            "definition": "Sequence-to-sequence models map input sequences to output sequences, commonly using encoder-decoder architectures, and are widely used in tasks like machine translation and text summarization.",
            "url": "https://arxiv.org/abs/1409.3215",
            "id": 193
        },
        {
            "name": "Recursive Neural Tensor Networks (RNTNs)",
            "definition": "RNTNs are neural networks that apply tensor-based transformations recursively over hierarchical structures like parse trees, capturing compositional semantics in natural language processing tasks.",
            "url": "https://nlp.stanford.edu/~socherr/EMNLP2013_RNTN.pdf",
            "id": 194
        },
        {
            "name": "Fine-Tuning",
            "definition": "Fine-tuning involves taking a pre-trained model and adapting it to a specific task by continuing the training process on a task-specific dataset, allowing for efficient learning with limited data.",
            "url": "https://huggingface.co/docs/transformers/training",
            "id": 195
        },
        {
            "name": "Foundation Model",
            "definition": "A foundation model is a large-scale model trained on broad data that can be adapted to a wide range of downstream tasks, serving as a base for various applications in AI.",
            "url": "https://en.wikipedia.org/wiki/Foundation_model",
            "id": 196
        },
        {
            "name": "Temperature",
            "definition": "In AI, temperature is a parameter that controls the randomness of predictions in models like language generators; higher values lead to more diverse outputs, while lower values make outputs more deterministic.",
            "url": "https://www.vellum.ai/llm-parameters/temperature",
            "id": 197
        },
        {
            "name": "Context Limit",
            "definition": "Context limit refers to the maximum number of tokens a model can consider in its input, affecting its ability to understand and generate text based on long contexts.",
            "url": "https://relevanceai.com/blog/how-to-overcome-context-limits-in-large-language-models",
            "id": 198
        },
        {
            "name": "Association Learning",
            "definition": "Association learning is a machine learning approach where the model discovers relationships between variables in data, often used in market basket analysis and recommendation systems.",
            "url": "https://en.wikipedia.org/wiki/Association_rule_learning",
            "id": 199
        },
        {
            "name": "PCA vs. LDA vs. SVD",
            "definition": "PCA, LDA, and SVD are dimensionality reduction techniques: PCA identifies directions of maximum variance, LDA finds linear combinations that best separate classes, and SVD decomposes matrices into singular vectors and values.",
            "url": "https://sebastianraschka.com/Articles/2014_pca_step_by_step.html",
            "id": 200
        },
        {
            "name": "DBSCAN",
            "definition": "DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a clustering algorithm that groups together points that are closely packed and marks points in low-density regions as outliers.",
            "url": "https://scikit-learn.org/stable/modules/clustering.html#dbscan",
            "id": 201
        },
        {
            "name": "Affinity Propagation",
            "definition": "Affinity Propagation is a clustering algorithm that identifies exemplars among data points and forms clusters by sending messages between points, without requiring the number of clusters to be specified beforehand.",
            "url": "https://scikit-learn.org/stable/modules/clustering.html#affinity-propagation",
            "id": 202
        },
        {
            "name": "ARIMA vs. SARIMA",
            "definition": "ARIMA models capture autocorrelations in time series data, while SARIMA extends ARIMA by incorporating seasonal components, making it suitable for data with seasonal patterns.",
            "url": "https://www.statsmodels.org/stable/examples/notebooks/generated/statespace_sarimax_stata.html",
            "id": 203
        },
        {
            "name": "AIC and BIC",
            "definition": "AIC (Akaike Information Criterion) and BIC (Bayesian Information Criterion) are metrics used to compare statistical models, balancing model fit and complexity to prevent overfitting.",
            "url": "https://en.wikipedia.org/wiki/Akaike_information_criterion",
            "id": 204
        },
        {
            "name": "White Noise",
            "definition": "White noise is a random signal with a constant power spectral density, meaning it has equal intensity at different frequencies, often used as a model for random disturbances in time series analysis.",
            "url": "https://en.wikipedia.org/wiki/White_noise",
            "id": 205
        },
        {
            "name": "ReLU, PReLU, ELU, GELU",
            "definition": "ReLU, PReLU, ELU, and GELU are activation functions in neural networks that introduce non-linearity; each has different properties affecting model performance and training dynamics.",
            "url": "https://ml-cheatsheet.readthedocs.io/en/latest/activation_functions.html",
            "id": 206
        },
        {
            "name": "Support Vector Classification",
            "definition": "Support Vector Classification is a supervised learning model that finds the optimal hyperplane separating data into classes, maximizing the margin between different class boundaries.",
            "url": "https://scikit-learn.org/stable/modules/svm.html",
            "id": 207
        },
        {
            "name": "Dark Knowledge",
            "definition": "Dark knowledge refers to the information captured by a neural network about the relationships between classes, as revealed by the soft targets (probability distributions) produced during training. This nuanced information can be used to train smaller models to mimic larger ones, a process known as knowledge distillation.",
            "url": "https://arxiv.org/abs/1503.02531",
            "id": 208
        },
        {
            "name": "ReAct prompting",
            "definition": "ReAct prompting is a technique combining reasoning and acting steps in language model prompts to improve multi-step problem solving and decision making.",
            "url": "https://www.promptingguide.ai/techniques/react",
            "id": 209
        },
        {
            "name": "Chain-of-thought (CoT) prompting",
            "definition": "Chain-of-thought prompting involves guiding language models to generate intermediate reasoning steps before producing a final answer, enhancing their ability to solve complex tasks.",
            "url": "https://arxiv.org/abs/2201.11903",
            "id": 210
        },
        {
            "name": "Negative Sampling",
            "definition": "Negative sampling is a technique used in training models, especially word embeddings, where a subset of negative examples is sampled to efficiently approximate a loss function.",
            "url": "https://arxiv.org/html/2402.17238v1",
            "id": 211
        },
        {
            "name": "Neural Machine Translation (NMT)",
            "definition": "Neural Machine Translation is an end-to-end learning approach for translating text from one language to another using neural networks.",
            "url": "https://en.wikipedia.org/wiki/Neural_machine_translation",
            "id": 212
        },
        {
            "name": "ElasticNet",
            "definition": "ElasticNet is a regularization technique that linearly combines L1 and L2 penalties to improve model prediction accuracy and feature selection.",
            "url": "https://scikit-learn.org/stable/modules/linear_model.html#elastic-net",
            "id": 213
        },
        {
            "name": "L1 (Lasso) and L2 (Ridge) regularization",
            "definition": "L1 regularization adds a penalty equal to the absolute value of coefficients (Lasso), promoting sparsity, while L2 regularization adds a penalty equal to the square of coefficients (Ridge), promoting smaller but nonzero coefficients.",
            "url": "https://en.wikipedia.org/wiki/Regularization_(mathematics)#L1_and_L2_regularization",
            "id": 214
        },
        {
            "name": "Huber Loss",
            "definition": "Huber loss is a robust loss function that is quadratic for small errors and linear for large errors, combining advantages of mean squared error and mean absolute error.",
            "url": "https://en.wikipedia.org/wiki/Huber_loss",
            "id": 215
        },
        {
            "name": "Cover’s theorem",
            "definition": "Cover’s theorem states that a complex pattern classification problem is more likely to be linearly separable in a higher-dimensional space.",
            "url": "https://en.wikipedia.org/wiki/Cover%27s_theorem",
            "id": 216
        },
        {
            "name": "Cross-entropy function",
            "definition": "Cross-entropy function measures the difference between two probability distributions, commonly used as a loss function for classification tasks.",
            "url": "https://en.wikipedia.org/wiki/Cross_entropy",
            "id": 217
        },
        {
            "name": "The dying ReLU problem",
            "definition": "The dying ReLU problem occurs when ReLU neurons output zero for all inputs during training, effectively becoming inactive and hindering learning.",
            "url": "https://towardsdatascience.com/the-dying-relu-problem-clearly-explained-42d0c54e0d24/",
            "id": 218
        },
        {
            "name": "Fully Connected Neural Network",
            "definition": "A fully connected neural network is a network architecture where each neuron in one layer is connected to every neuron in the next layer.",
            "url": "https://deeplearningmath.org/general-fully-connected-neural-networks.html",
            "id": 219
        },
        {
            "name": "Sequential model-based optimization (SMBO)",
            "definition": "SMBO is an optimization strategy that iteratively builds a surrogate model to guide the search for the best hyperparameters or configurations.",
            "url": "https://arxiv.org/abs/2003.13826",
            "id": 220
        },
        {
            "name": "Evolutionary Optimization",
            "definition": "Evolutionary optimization uses mechanisms inspired by biological evolution, such as mutation and selection, to iteratively improve candidate solutions.",
            "url": "https://arxiv.org/abs/2403.02985",
            "id": 221
        },
        {
            "name": "Search space",
            "definition": "Search space is the set of all possible candidate solutions or hyperparameter configurations considered during an optimization or learning process.",
            "url": "https://www.sciencedirect.com/topics/engineering/search-space",
            "id": 222
        },
        {
            "name": "AI workload mobility",
            "definition": "AI workload mobility refers to the ability to transfer AI tasks and models seamlessly across different computing environments or hardware platforms.",
            "url": "https://www.tierpoint.com/blog/ai-workloads/",
            "id": 223
        },
        {
            "name": "Gaussian Mixture Models (GMM)",
            "definition": "Gaussian Mixture Models are probabilistic models that represent a distribution as a mixture of multiple Gaussian components, often used for clustering.",
            "url": "https://en.wikipedia.org/wiki/Mixture_model#Gaussian_mixture_model",
            "id": 224
        },
        {
            "name": "K-Medoids",
            "definition": "K-Medoids is a clustering algorithm similar to K-Means but uses actual data points as cluster centers, making it more robust to noise and outliers.",
            "url": "https://en.wikipedia.org/wiki/K-medoids",
            "id": 225
        },
        {
            "name": "Agglomerative Clustering vs. Divisive Clustering",
            "definition": "Agglomerative clustering builds clusters by iteratively merging data points, while divisive clustering splits data into clusters from the top down.",
            "url": "https://en.wikipedia.org/wiki/Hierarchical_clustering#Agglomerative_clustering",
            "id": 226
        },
        {
            "name": "Quantization",
            "definition": "Quantization is the process of mapping input values from a large set to output values in a smaller set, often used to reduce model size and improve efficiency.",
            "url": "https://en.wikipedia.org/wiki/Quantization_(signal_processing)",
            "id": 227
        },
        {
            "name": "Pseudo-label",
            "definition": "Pseudo-labeling is a semi-supervised learning technique where a model assigns labels to unlabeled data based on its predictions to augment training.",
            "url": "https://arxiv.org/abs/1908.02983",
            "id": 228
        },
        {
            "name": "Centroid",
            "definition": "A centroid is the center point of a cluster, calculated as the mean of all points in that cluster.",
            "url": "https://en.wikipedia.org/wiki/Centroid",
            "id": 229
        },
        {
            "name": "Affinity",
            "definition": "Affinity measures the similarity or closeness between data points or clusters, used in clustering algorithms.",
            "url": "https://en.wikipedia.org/wiki/Clustering_algorithms#Affinity_propagation",
            "id": 230
        },
        {
            "name": "Linkage: Single, Complete, Average, and Ward",
            "definition": "Linkage methods define how distances between clusters are computed in hierarchical clustering: single linkage uses minimum distance, complete uses maximum, average uses mean distances, and Ward minimizes variance within clusters.",
            "url": "https://www.geeksforgeeks.org/machine-learning/ml-types-of-linkages-in-clustering/",
            "id": 231
        }

    ]

    # Select a candidate word from word list
    candidate_word = random.choice(word_list)

    # Query db for current used word list
    used_list_search = db.search(User.used.exists())
    if used_list_search:
        used_list = used_list_search[0]["used"]
    else:
        used_list = []

    # If length of word list and length of used list is equal, erase used list and start over
    if len(used_list) == len(word_list):
        used_list = []

    # If random choice is already in used list, choose again
    while candidate_word["id"] in used_list:
        candidate_word = random.choice(word_list)

    # Solidify choice
    word = candidate_word

    # Add new choice to used list and to db
    used_list.append(word["id"])
    db.upsert({"used": used_list}, User.used.exists())

    return word
