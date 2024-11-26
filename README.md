# gen_ai_prompt_for_logical_problem

prompting gen AI to solve logical problem, namely the Missionary and Cannibals Problem

## notes

output: complete list of actions, cannot be something like "and so on..."

## problem text

```txt
30 sisters and 30 brothers must cross a river using a boat which can carry at most four
people, under the constraint that, for both banks, if there are sisters present on the bank,
they cannot be out-numbered by brothers. How do they cross the river?
```

To solve the problem, you can only use the above description as input to your generative
AI tools. You can use general prompts such as “solve the problem step by step”. You
should not suggest solutions such as “start by moving 2 brothers and 2 sisters to the
other side, then bring 2 sisters back and so on”. The final solution needs to be a sequence
of moves.

## objective

- prompt the AI to solve it, result should be a step by step solution

## todos

- read the bfs solution
- prompting by hand
- ~~write code for simulation~~
- use azure api to repeatedly prompt, and use answer as input to simlution
  - obtain azure api

## running the simulator

```ps
py sim.py
```

## presentation

5 minutes presentation

## ref

<https://github.com/Bishalsarang/Missionaries-and-Cannibals-Problem>
