# stellar_calculator
This calculator uses transit photometry data to calculate the semi-major axis and planet radius of a star-exoplanet system.

It takes in the following values:
| Value | Unit      | Description    |
| ----- | --------- | -------------- |
| T     | seconds   | Orbital period |
| M     | kilograms | Stellar mass   |
| R_S   | metres    | Stellar radius |
| t     |           | transit depth  |

The program produces the following values:
| Value | Unit   | Description     |
| ----- | ------ | --------------- |
| a     | metres | Semi-major axis |
| R_P   | metres | Planet radius   |
