# LEGO
MircoPython scripts for LEGO hubs using [pybricks](https://pybricks.com) framework.

## Hub Mode
Hub internal mode's state diagram.

- Off
- Program mode
- Running mode

```mermaid
stateDiagram-v2
[*] --> Off
Off --> On: Press
On --> Off: Long Press

state On {
[*] --> Program
Program --> Run: Press
Run --> Program: Press
}
```

## Projects

- [Audi RS Q e-tron](/42160)

