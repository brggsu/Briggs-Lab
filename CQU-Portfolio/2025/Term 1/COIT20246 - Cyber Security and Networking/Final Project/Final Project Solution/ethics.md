# Ethical Issues
This section discusses the different ethical issues that arise in the scenario, focusing on data privacy, security, and responsible technology use.  
  
[Data Privacy](#data-privacy-and-security-issues) | [Plan](./plan.md) | [Network Design](./network.md) | [Cloud Services](./cloud.md) | [Security](./security.md) | [Reflections](./reflections.md) | [Return to index](./README.md)
      
               
## Data Privacy Concerns

Truelec collects and manages sensitive information through its booking application, HR systems, and internal security infrastructure. This includes:

- **Customer data:** names, contact details, and payment information.
- **Employee data:** HR and payroll records, identification details, and personal information.
- **Operational data:** contracts, supplier records, CCTV footage, RFID access logs, and IoT sensor outputs.

The ethical responsibility lies in ensuring that this information is collected with informed consent, stored securely, and used only for legitimate business purposes. Collecting or processing data without transparency would breach both trust and ethical obligations.

## Risks of Unauthorised Access

Truelec faces several risks if data privacy is not managed effectively:
- Cyberattacks such as ransomware targeting databases and servers.
- Insider misuse of sensitive HR or customer data.
- Accidental leakage through misconfigured WiFi or cloud services.

The impact of such breaches would extend to:
- Customers (identity theft, financial fraud, loss of trust).
- Employees (misuse of payroll/HR records, reputational harm).
- The business (legal liability, regulatory fines, reputational damage, loss of contracts).

## Data Protection Regulations

Truelec must comply with the Australian Privacy Principles (APPs) under the Privacy Act 1988 (Cth), which requires organisations to:

- Limit collection to necessary data.
- Protect personal information through robust security.
- Notify the Office of the Australian Information Commissioner (OAIC) and affected parties of any Notifiable Data Breach.

If working with overseas clients or contractors, Truelec may also need to consider international frameworks such as the European Union General Data Protection Regulation (EU GDPR), which governs cross-border transfers of personal data.


## Protecting Data Privacy in the Proposed Design

We designed our solution to protect the privacy of both employee and customer data. Cloud providers Microsoft Azure hold compliance certifications including GDPR, ISO 27001, and the APPs, supporting regulatory alignment.

Key measures include:

- **Access Control:** Azure Active Directory will restrict access to authorised staff only.
- **Encryption:** Sensitive data (HR, financial, customer contact details) will be encrypted at rest and in transit (TLS 1.2+).
- **Audit Logging:** Access to data will be logged and reviewed for accountability.

## Security Measures

To address the risks, our implementation will include:

- **Firewalls & VPNs:** Restrict external access and provide secure tunnels for remote employees.
- **Multi-Factor Authentication (MFA):** Mandatory for administrative accounts and remote access.
- **Continuous Monitoring:** Microsoft Azure Security Center for real-time threat detection and incident response.
- **Patch Management:** Regular updates to servers and network devices to mitigate vulnerabilities.

## Ethical Considerations

While technical controls and compliance frameworks are essential, Truelec also has a broader ethical responsibility in the way it manages information. This begins with transparency: **Employees** and **Customers** should clearly understand what data is being collected, the reasons for its collection, and how it will be used. Equally important is data minimisation, meaning that the company should only gather and retain information that is genuinely necessary for its operations. 

Ethical practice also involves avoiding excessive surveillance; monitoring activities should remain focused on maintaining system security and performance rather than intruding on employee privacy. Finally, sustainability is an important consideration. By right-sizing cloud resources and adopting energy-efficient infrastructure, Truelec can reduce its environmental footprint and demonstrate a commitment to responsible business practices that extend beyond immediate technical needs.fficient infrastructure to reduce environmental impact.

## Conclusion

By combining strong compliance practices, technical safeguards, and ethical commitments, Truelec can ensure that its handling of sensitive customer and employee data upholds both legal obligations and social trust.

## References


Australian Government 2023, Privacy Act 1988 (Cth), Federal Register of Legislation, viewed 3 October 2025, <https://www.legislation.gov.au/Series/C2004A03712>

Australian Government 2024, Notifiable Data Breaches Scheme 2024, Office of the Australian Information Commissioner (OAIC), viewed 3 October 2025, <https://www.oaic.gov.au/privacy/notifiable-data-breaches>

European Commission 2024, EU General Data Protection Regulation (GDPR), European Union, viewed 3 October 2025, <https://gdpr.eu/>

Microsoft 2025, Azure shared responsibility model, viewed 3 October 2025, <https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility>

Office of the Australian Information Commissioner 2025, Australian privacy principles, viewed 3 October 2025, <https://www.oaic.gov.au/privacy/the-privacy-act/australian-privacy-principles>

