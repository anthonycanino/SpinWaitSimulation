For Praveen.

# General Instructions

## Getting TSC Frequency

I have created a project, Freq, which will help get a TSC frequence for the system. Please build with Visual Studio (I used 2022) by opening `Freq/Freq.vcxproj` and building with Release mode. That should create `Freq/x64/Release/Freq.exe`. Just run the executable, and it should print out something like 

```
Cycles: 20000404154 Freq: 2000040415 HZ Freq: 2 GZ
```

Please copy the HZ number (so 2000040415 above) and change the value at `PrimeNumbers/t_join.h` line 158 to this value. So, change 

```
const unsigned long long TSC_FREQUENCY_IN_HZ = 2e9;
```

to

```
const unsigned long long TSC_FREQUENCY_IN_HZ = 2000040415;
```

with 2000040415 replaced by the value on your system.

## PrimeNumbers Project

We will build and run the PrimeNumbers subproject. Please build with Visual Studio (I used 2022) by opening `PrimeNumbers/PrimeNumbers.vcxproj` and building with Release mode. That should create `PrimeNumbers/x64/Release/PrimeNumbers.exe`.

Please test to make sure it runs with the following command: `PrimeNumbers/x64/Release/PrimeNumbers.exe --ht 1 --input_count 20000 --complexity 5`.

In `PrimeNumbers`, there is a file called `res.csv`. Please remove this file before starting the series of runs: it accumulates the results, and will be useful to have to associate the power readings with. 

### Cases

We will evaluate the following parameters

- `complexity` , which determines the computation of prime numbers per thread. A higher results in average longer wait times per thread before moving on to the next prime number computation.
 - we will run with `{20}`

- `join_type`, which determines the implementation of the "spin lock"
  - we will run with `{1, 2, 7, 8, 9, 10}`

- `wait_count`, which determines how long a thread will wait before going into a hard sleep (for umwait, it is the associated wait time for wake, in offset of TSC)
  - we will run with `{1, 2, 5, 10}`

- `umwait_power_state`, which determines the C0 state for tpause/umwait

  - we will run with `{0, 1}`

- `gen_file`, which loads a pre-generated list of prime numbers. the input_count and thread_count must match that in the file.

  - we will point to the supplied `num.txt` file

As a first pass, lets only vary the `join_type` and `wait_count`. 

We will use the following join types, 1 (current impl), 2 (pause), 7 (umwait, spin loop with hard wait), 8 (umwait, only spin), 9 (umwait, no spin, hard wait), 10 (umwait, no spin, no hard wait). 

We want to simulate a `1us`, `10us`, and `1ms` wait time, so for wait_count we will use...

### The Actual Commands

For ease of use, I've laid out the actual commands to run...


The following is the full set of commands using a wait_count as 1 (which is 1us). 

```powershell
# With umwait powerstate 0
x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 1 --wait_count 1 --umwait_power_state 0 --gen_file num.txt

x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 2 --wait_count 1 --umwait_power_state 0 --gen_file num.txt

x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 7 --wait_count 1 --umwait_power_state 0 --gen_file num.txt

x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 8 --wait_count 1 --umwait_power_state 0 --gen_file num.txt

x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 9 --wait_count 1 --umwait_power_state 0 --gen_file num.txt

x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 10 --wait_count 1 --umwait_power_state 0 --gen_file num.txt

# With umwait powerstate 1
x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 1 --wait_count 1 --umwait_power_state 1 --gen_file num.txt

x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 2 --wait_count 1 --umwait_power_state 1 --gen_file num.txt

x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 7 --wait_count 1 --umwait_power_state 1 --gen_file num.txt

x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 8 --wait_count 1 --umwait_power_state 1 --gen_file num.txt

x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 9 --wait_count 1 --umwait_power_state 1 --gen_file num.txt

x64/Release/PrimeNumbers.exe --ht 1 --input_count 100000 --complexity 15 --join_type 10 --wait_count 1 --umwait_power_state 1 --gen_file num.txt
```


The entire block of commands must be repeated, but for different `wait_count`, which would be `2`, `5`, and `10` for `2us`, `5us` and `10us` respectively.