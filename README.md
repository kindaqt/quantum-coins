# Quantum Coin Flip

This is a quantum toy app that showcases some beginner concepts of quantum computing such as superposition, measurement, non-locality, non-temporality, and entanglement.

## Quantum Coins 

Quantum coins are special in the following ways:

- When Quantum Coins are flipping they are in superposition.
- When Quantum Coins collide while they are flipping they become entangled.
- When a Quantum Coin hits the ground it is measured. Measuring an entangled Quantum Coin has the same effect as measuring an entangled qubit.

### States

| Coin          | Bit       | State       |
| ------------- | --------- | ----------- |
| Heads         | `0`       | `[1,0]`     |
| Tails         | `1`       | `[0,1]`     |
| Superposition | `0` & `1` | `[0.5,0.5]` |

### Workflow

- User chooses the number of coins.
- User chooses the initial state of each coin.
- User can choose to entangle 2 coins.
- User flips the coins.

## Tech

This is a flask app. Click [here](https://flask.palletsprojects.com/en/1.1.x/) for more information on Flask.

## Start

### Prod

```
export FLASK_APP=coin.py
flask run
```

### Debug Mode

```
export FLASK_APP=coin.py
export FLASK_ENV=development
flask run
```

Debug mode does the following things:

- it activates the debugger
- it activates the automatic reloader
- it enables the debug mode on the Flask application.

## Q Object

```
{
  qobj_id: "e9c7d67b-3163-4bf3-8dfc-9f2af43083bf",
  header: {},
  config: {
    shots: 1024,
    memory: false,
    parameter_binds: [],
    init_qubits: false,
    memory_slots: 0,
    n_qubits: 3,
  },
  schema_version: "1.2.0",
  type: "QASM",
  experiments: [
    {
      config: { n_qubits: 3, memory_slots: 0 },
      header: {
        qubit_labels: [
          ["q", 0],
          ["q", 1],
          ["q", 2],
        ],
        n_qubits: 3,
        qreg_sizes: [["q", 3]],
        clbit_labels: [],
        memory_slots: 0,
        creg_sizes: [],
        name: "circuit1",
        global_phase: 0,
      },
      instructions: [
        { name: "h", qubits: [0] },
        { name: "h", qubits: [0] },
        { name: "h", qubits: [1] },
        { name: "h", qubits: [2] },
      ],
    },
  ],
}
```