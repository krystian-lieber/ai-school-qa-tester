# Fine-tuning samples

## Dataset

The finetuning dataset used to fine-tune the model was prepared using gpt-4o and Cluaude Opus.

## Baseline

Used gpt-4o and gpt-3.5-turbo to generate tests. Generating tests with gpt-4o costs about 0.05$ while with 3.5-turbo it costs about 0.015$.

## Finetuned 1

Run file `tester_finetuned1.py`, tests in `finetuned1`
This model was trained on sample data only, and system prompt was used.
Finetuning parameters:

- Trained tokens: 54,960
- Epochs: 15
- Batch size: 3
- LR multiplier: 0.3
- Seed: 514023459

https://smith.langchain.com/public/16063e13-226b-4393-ba34-d05e5a0a5f28/r

It did not work, the fine-tuned model was not able to generate the correct tests. It just repeated writing scenarios:

```python
  - Test the function with typical inputs.
  - Test the function with edge cases.
  - Test the function with invalid inputs.
```

The final tests are correct but it is because the agent is controlled by gpt-4o and it decided to ditch the output of the fine-tuned model and did it on its own.

## Finetuned 2

Run file `tester_finetuned2.py`, tests in `finetuned2`.
This model was trained on enhanced data. The system prompt was removed.
Finetuning parameters:

- Trained tokens: 360,150
- Epochs: 15
- Batch size: 3
- LR multiplier: 0.3
- Seed: 674350684

https://smith.langchain.com/public/d3d467cf-2788-4613-a72a-70e956b283c7/r

The content improved it looks like actual tests:

```python
    def test_factorial_positive_positive(self):
        self.assertEqual(factorial(5) * factorial(4), 120)
```

But of course, it is incorrect as it should be 2880.
The final tests are correct but it is because the agent is controlled by gpt-4o and it decided to ditch the output of the fine-tuned model and did it on its own.

## Finetuned 3

Run file `tester_finetuned3.py`, tests in `finetuned3`
This model was trained on enhanced data. The system prompt was removed.
Finetuning parameters:

- Trained tokens: 72,030
- Epochs: 3
- Batch size: 1
- LR multiplier: 16
- Seed: 472235533

https://smith.langchain.com/public/e58b49fc-352a-4e4f-bbf6-4b316b5a7024/r

The content improved it looks like actual tests and the values are correct:
```python
    def test_factorial_positive_number(self):
        self.assertEqual(factorial(5), 120)
```
The gpt4o model used the test just cutting the output of the fine-tuned model, to extract just the test.

It was a lot cheaper, costing only $0.035. Which means it is 14 times cheaper than gpt-4o, and 5 times cheaper than gpt-3.5-turbo. It does not include the fine-tuning cost, but those would be quickly recouped when generating many tests.
