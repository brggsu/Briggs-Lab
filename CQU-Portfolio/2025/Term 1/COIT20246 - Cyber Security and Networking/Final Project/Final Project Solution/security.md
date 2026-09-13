# Security
This section gives a cyber security risk assessment for the company and recommended security controls.

[Risk Assesment](#risk-assessment) | [Security Controls](#security-controls) | [Plan](./plan.md) | [Network Design](./network.md) | [Cloud Services](./cloud.md) | [Ethics](./ethics.md) | [Reflection](./reflection.md) | [Return to index](./README.md)

## Risk Assessment
Risk Assessment File: [Risk Assessment File](./images/security_files/SYD-Group-31-Risk-Assessment.xlsx)

## Security Controls

Based on our risk assessment, the data asset with the highest risk (Rank 1) is:
- **Asset**: Employee HR records
- **Threat:** Software attacks (Ransomware encrypting databases containing Employee HR records)
- **Likelihood:** High
- **Impact:** Very High
- **Risk rating:** Very High

## Recommended Security Controls

Three useful controls to mitigate this risk from NIST SP 800-53 are:

1. **SC-28: Protection of Information at Rest**
- **Explanation:** Encrypting the HR database ensures that even if ransomware or attackers gain access, the records remain unreadable without keys. This reduces the impact of exfiltration or extortion attempts. In the project scenario, AES-256 encryption should be applied at the database and storage layer on the central server, with encryption keys managed securely via a Hardware Security Module (HSM) or Azure Key Vault for cloud backups. Encrypted backups must integrate seamlessly with existing HR systems to avoid workflow disruption. This control directly reduces the risk of data disclosure but may introduce performance slowdowns during intensive queries, such as payroll processing, and HR staff may face additional authentication prompts when accessing decrypted data (NIST, 2020).

2. **CP-9: Information System Backup**
- **Explanation:** Regular, secure backups ensure resilience against ransomware by allowing restoration of HR records without ransom payments. In this project, daily incremental and weekly full backups of HR data should be scheduled, with copies stored in a segregated backup VLAN and replicated to an offsite Azure Backup Vault with immutable storage enabled. Access to backup servers must be tightly restricted behind a dedicated firewall. This approach provides business continuity, though users may experience temporary downtime when data restoration is required, and backup cycles may cause minor slowdowns during HR record updates (NIST, 2020).

3. **AC-3: Access Enforcement**
- **Expanlantion:** Limiting access to HR records reduces the likelihood of ransomware spreading through compromised user accounts. Role-based access control (RBAC) will ensure only HR staff have permissions, supported by mandatory multi-factor authentication (MFA). Logs of access should be monitored via a SIEM solution. Network segmentation further protects HR systems by restricting access to the HR VLAN from authorised HR endpoints only. This directly prevents lateral movement by attackers but can inconvenience HR staff who require temporary cross-department access and may increase IT support workload for access requests (NIST, 2020).


## Summary
The combination of SC-28 (encryption), CP-9 (secure backups), and AC-3 (access control) significantly reduces both the likelihood and impact of ransomware attacks on HR records. Although these measures may slightly slow system performance and introduce usability challenges, the trade-off ensures the confidentiality, integrity, and availability of the organisation’s most sensitive employee data.

## References

Microsoft 2025, Azure Key Vault documentation, viewed 3 October 2025, <https://learn.microsoft.com/en-us/azure/key-vault/>

NIST 2020, Security and privacy controls for information systems and organizations (NIST SP 800-53 Rev. 5), National Institute of Standards and Technology, U.S. Department of Commerce, viewed 3 October 2025, <https://doi.org/10.6028/NIST.SP.800-53r5>

Stallings, W 2020, Effective cybersecurity: a guide to using best practices and standards, Addison-Wesley Professional, viewed 3 October 2025, <https://www.pearson.com/en-us/subject-catalog/p/effective-cybersecurity/P200000008367/9780134772806>
 
