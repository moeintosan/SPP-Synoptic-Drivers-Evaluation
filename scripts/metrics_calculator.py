"""
Precipitation Performance Evaluation Metrics Calculator
Associated with: "Linking the skill of multi-satellite precipitation estimates to the synoptic drivers..." (2026)
Author: Moein Tosan
"""

import numpy as np


class HydroMetrics:

    def __init__(self, satellite_data, gauge_data):
        """
        Initialize with satellite and rain gauge daily time series (numpy arrays).
        """
        self.s = np.array(satellite_data)
        self.g = np.array(gauge_data)

    def calculate_continuous(self):
        """
        Calculates Pearson Correlation Coefficient (CC), Root Mean Square Error (RMSE),
        and Normalized Mean Bias (NMB) based on paper Table 2.
        """
        # Pearson Correlation Coefficient (CC)
        cc = np.corrcoef(self.s, self.g)[0, 1] if len(self.s) > 1 else 0.0

        # Root Mean Square Error (RMSE)
        rmse = np.sqrt(np.mean((self.s - self.g) ** 2))

        # Normalized Mean Bias (NMB %)
        sum_g = np.sum(self.g)
        nmb = ((np.sum(self.s - self.g)) / sum_g) * 100 if sum_g != 0 else 0.0

        return {"CC": round(cc, 3), "RMSE": round(rmse, 3), "NMB_%": round(nmb, 2)}

    def calculate_categorical(self, threshold=1.0):
        """
        Calculates Probability of Detection (POD), False Alarm Rate (FAR),
        and Critical Success Index (CSI) for a given rain threshold (default = 1.0 mm/day).
        """
        hits = np.sum((self.s >= threshold) & (self.g >= threshold))
        false_alarms = np.sum((self.s >= threshold) & (self.g < threshold))
        misses = np.sum((self.s < threshold) & (g >= threshold))

        pod = hits / (hits + misses) if (hits + misses) > 0 else 0.0
        far = (
            false_alarms / (hits + false_alarms)
            if (hits + false_alarms) > 0
            else 0.0
        )
        csi = (
            hits / (hits + false_alarms + misses)
            if (hits + false_alarms + misses) > 0
            else 0.0
        )

        return {"POD": round(pod, 3), "FAR": round(far, 3), "CSI": round(csi, 3)}
