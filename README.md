# Polar Code Encoding and Decoding Project

## Objective of the Project
The aim of this project was to develop an efficient algorithm for encoding and decoding Polar Codes, utilizing Successive Cancellation (SC) and Successive Cancellation List (SCL) decoding techniques. This project includes the implementation of Monte Carlo simulations over an Additive White Gaussian Noise (AWGN) channel to validate the algorithm’s performance. Additionally, a reliability sequence generation code was also developed. The project was a comprehensive team effort, including the creation of a detailed report and presentation explaining the encoding and decoding processes in Polar Codes.

## Description of the Project
Polar Codes are a type of error-correcting code that have gained significant attention in communication theory due to their capacity-approaching performance under SC and SCL decoding. They are particularly useful for encoding and transmitting messages in noisy communication channels.

## Encoding
The encoding process involves transforming the input message into a codeword using the Polar transformation. This process increases the robustness of the message against noise in the transmission channel.

## Decoding
### Successive Cancellation (SC) Decoding: 
This is the basic decoding technique for Polar Codes. It decodes each bit of the received message successively, making decisions based on previously decoded bits.
### Successive Cancellation List (SCL) Decoding: 
This technique improves upon SC by considering multiple decoding paths simultaneously. It retains a list of potential codewords, thereby increasing the likelihood of correct decoding.
### Reliability Sequence
A reliability sequence was generated to enhance the performance of Polar Codes. This sequence identifies the most reliable positions for placing the information bits, optimizing the decoding process.

### Monte Carlo Simulation
Monte Carlo simulations were performed to evaluate the performance of the encoding and decoding algorithms over an AWGN channel. These simulations helped in calculating the expected error probabilities and provided a comprehensive understanding of the algorithms' effectiveness.

### Time-Space Complexity
The overall time complexity of the decoding algorithm depends on the number of simulations and the specific decoding technique used. For SC decoding, the complexity is relatively lower compared to SCL decoding, which maintains multiple decoding paths.

Time Complexity: O((number of simulations) * (N) * (max_it)), where N is the block length and max_it is the maximum iterations.
Space Complexity: O(N), due to the storage requirements of the reliability sequence and decoding paths.

## Contents
- Encoding Algorithm: Implementation of the Polar Code encoding process.
- Successive Cancellation Decoder: Performs decoding using the SC decoding technique.
- Successive Cancellation List Decoder: Performs decoding using the SCL decoding technique.
- Reliability Sequence Generator: Generates the reliability sequence for optimal decoding.
- MonteCarlo Simulation: MATLAB script for performing Monte Carlo simulations over an AWGN channel.
- Simulation Results: Comparison of simulation results with theoretical expectations over different noise levels.
## Next Steps
 Space Complexity Optimization: Improve the space complexity without increasing the time complexity by optimizing the data structures used.
 Enhanced Decoding Techniques: Explore and implement advanced decoding techniques to further improve the error-correcting performance of Polar Codes.
This project has provided valuable insights into the implementation and performance of Polar Codes, highlighting the importance of efficient encoding and decoding techniques in modern communication systems.





