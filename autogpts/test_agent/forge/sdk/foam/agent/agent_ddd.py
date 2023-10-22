from foam.ddd_models import *

ddd_instance = DDD(
    aggregates=[
        Aggregate(
            root_entity="Agent",
            entities=[
                Entity(
                    name="Agent",
                    definition="An Agent entity based on the CoALA framework",
                    business_functions=[
                        BusinessFunction(
                            name="CreateAgent",
                            parameters=[{"parameter": "agent", "type": "Agent"}],
                            definition="Create an agent according to the CoALA framework",
                            contract={
                                "ensure": [Require(condition="lambda result: result is not None")],
                                "require": [Require(condition="lambda agent: agent is not None")],
                            },
                        )
                    ],
                    factories=[
                        Factory(
                            name="CreateAgent", parameters=[{"parameter": "name", "type": "string"}]
                        )
                    ],
                    repositories=[
                        Repository(
                            name="AgentRepository",
                            methods=[
                                Method(
                                    name="find_by_name",
                                    parameters=[{"parameter": "name", "type": "string"}],
                                )
                            ],
                        )
                    ],
                )
            ],
            value_objects=[
                ValueObject(
                    name="Memory",
                    definition="A Memory value object, contains various types of memory modules",
                    properties=[
                        {"name": "working_memory", "type": "dict"},
                        {"name": "long_term_memory", "type": "dict"},
                    ],
                ),
                ValueObject(
                    name="Action",
                    definition="An Action value object, embodies agent activities",
                    properties=[
                        {"name": "type", "type": "string"},
                        {"name": "parameters", "type": "dict"},
                    ],
                ),
                ValueObject(
                    name="Environment",
                    definition="An Environment value object, denotes different external environments",
                    properties=[
                        {"name": "type", "type": "string"},
                        {"name": "properties", "type": "dict"},
                    ],
                ),
                ValueObject(
                    name="Decision",
                    definition="A Decision value object, encapsulates decision-making process",
                    properties=[
                        {"name": "evaluations", "type": "list"},
                        {"name": "proposals", "type": "list"},
                        {"name": "simulations", "type": "list"},
                    ],
                ),
            ],
            aggregate_business_functions=[
                BusinessFunction(
                    name="InitializeMemory",
                    parameters=[
                        {"parameter": "agent", "type": "Agent"},
                        {"parameter": "memory", "type": "Memory"},
                    ],
                    definition="Initialize the agent\\'s memory modules within the CoALA framework",
                    contract={
                        "ensure": [Require(condition="lambda result: isinstance(result, Memory)")],
                        "require": [
                            Require(
                                condition="lambda agent, memory: agent is not None and memory is not None"
                            )
                        ],
                    },
                ),
                BusinessFunction(
                    name="DefineActionSpaces",
                    parameters=[
                        {"parameter": "agent", "type": "Agent"},
                        {"parameter": "action", "type": "Action"},
                    ],
                    definition="Define and structure the agent\\'s action spaces",
                    contract={
                        "ensure": [Require(condition="lambda result: result is True")],
                        "require": [
                            Require(
                                condition="lambda agent, action: agent is not None and action is not None"
                            )
                        ],
                    },
                ),
                BusinessFunction(
                    name="GroundingActions",
                    parameters=[
                        {"parameter": "agent", "type": "Agent"},
                        {"parameter": "environment", "type": "Environment"},
                    ],
                    definition="Procedures for grounding actions, allowing the agent to interact with external environments",
                    contract={
                        "ensure": [Require(condition="lambda result: result is True")],
                        "require": [
                            Require(
                                condition="lambda agent, environment: agent is not None and environment is not None"
                            )
                        ],
                    },
                ),
                BusinessFunction(
                    name="RetrievalActions",
                    parameters=[{"parameter": "agent", "type": "Agent"}],
                    definition="Retrieval procedures to read information from long-term memories into the working memory",
                    contract={
                        "ensure": [Require(condition="lambda result: result is True")],
                        "require": [Require(condition="lambda agent: agent is not None")],
                    },
                ),
                BusinessFunction(
                    name="ReasoningActions",
                    parameters=[
                        {"parameter": "agent", "type": "Agent"},
                        {"parameter": "memory", "type": "Memory"},
                    ],
                    definition="Reasoning procedures to process working memory contents and generate new knowledge",
                    contract={
                        "ensure": [Require(condition="lambda result: result is True")],
                        "require": [
                            Require(
                                condition="lambda agent, memory: agent is not None and memory is not None"
                            )
                        ],
                    },
                ),
                BusinessFunction(
                    name="LearningActions",
                    parameters=[
                        {"parameter": "agent", "type": "Agent"},
                        {"parameter": "memory", "type": "Memory"},
                    ],
                    definition="Enable the agent to learn by updating long-term memory",
                    contract={
                        "ensure": [Require(condition="lambda result: result is True")],
                        "require": [
                            Require(
                                condition="lambda agent, memory: agent is not None and memory is not None"
                            )
                        ],
                    },
                ),
                BusinessFunction(
                    name="DecisionMaking",
                    parameters=[{"parameter": "agent", "type": "Agent"}],
                    definition="Design a decision-making process that allows the agent to choose actions",
                    contract={
                        "ensure": [
                            Require(condition="lambda result: isinstance(result, Decision)")
                        ],
                        "require": [Require(condition="lambda agent: agent is not None")],
                    },
                ),
            ],
        )
    ]
)
