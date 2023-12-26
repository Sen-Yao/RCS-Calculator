# RCS-Calculator

A Python script for calculating the Radar Cross-Section (RCS) of an object using CST farfield data across different frequencies. This project was developed for Professor Ma Hong's "Electromagnetic Fields and Electromagnetic Waves" course at EIC, HUST in 2021.

## Theoretical Knowledge

Radar Cross-Section (RCS), denoted by σ and also known as radar signature, is a measure of an object's detectability by radar. For more information, see [Radar Cross-Section on Wikipedia](https://en.wikipedia.org/wiki/Radar_cross_section)

Given the incident electric field vector Ei and the incident angles (θi, φi), the two-station RCS in the scattering direction (θs, φs) at a far field distance R can be expressed as:

$$\sigma(\theta_s,\phi_s|\theta_i,\phi_i)=4\pi R^2 \frac{|E_\theta(\theta_s,\phi_s)|^2+|E_\phi(\theta_s,\phi_s)|^2}{|E_i(\theta_s,\theta_i)|^2}$$

The total RCS is given by:

$$\sigma(\theta_i,\theta_i)=\int_0^{2\pi}d\phi_s\int_0^\pi \frac{|E_\theta(\theta_s,\phi_s)|^2+|E_\phi(\theta_s,\phi_s)|^2}{|E_i(\theta_s,\theta_i)|^2} R^2\sin \theta_s d\theta_s$$

This script calculates the RCS for varying scattering directions (θs, φs) using Eφ and Eθ data from CST. Approximating the integral with a sum over sufficiently dense data points allows for the computation of total RCS.

## Requirements

- python 3.8

## Usage

Preset electric field intensity data calculated by CST is integrated into the /data folder. To calculate RCS based on your custom electric field intensity data, use the --path argument to specify the data folder. If you have RCS data in the scattering direction calculated by CST, export them and place them in the data folder. The script can automatically detect and process scattering direction RCS.

To run the script, use the following command:

```
main.py [--path] [--Ei] [--R]
```

*optional arguments*:


``--path -p ``    Path to electric field intensity data's folder

``--Ei -E``    Mode of incident electric field

``--R -R``    Distance between the far field point and the target.

Example Usage:

```
python main.py -E 1 -R 1
```

## Contributors

- Zhang Yezheng（ https://github.com/pxxxl ）
- Li Zhiwei （ https://github.com/mj3622 ）
- Wei Yifan
- Chen Shuaifan
