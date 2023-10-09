# This is readme for this project - Djamal Santos

## Engineering Tech Spec – Phase I

### Description
The project is to implement a checkout with Mpesa service to support B2C (Business-to- Customer) and C2B (Customer-to-Business) models. for that, the goals are, Enable customers to make payments using Mpesa API in the B2C model, Enable businesses to make payments to customers using Mpesa API in the B2C model, and Allow businesses to receive payments using Mpesa API in the C2B model.

To achieve all the defined goals, we need to divide the problem into small problems, and we will increase the complexity.

### Implementation and rollout plan
The implementation and rollout plan should be filled out based on the size and scope of the project. The plan should be gradually updated as the project progresses towards launch. and If an extensive migration is necessary, a separate tech spec should be created and link to it should be included on the principal plan. Instructions for rolling back in the event of an unsuccessful migration should also be provided.

Instructions for supporting an incremental release, if needed, should be provided. It will follow a process of continuous development and the use of good practices is crucial. As a basis, you will use Semantic Versioning as a standard for versioning APIs. That consists of three numbers (e.g. 1.2.3), which represent the version as follows: 
- The first number (1) is the major version and is incremented when changes occur that
are incompatible with previous versions.
- The second number (2) is the secondary version and is incremented when backward-
compatible functionalities are added.
- The third number (3) is the patch version and is incremented when bug fixes are made
backwards compatible.
For example: v1.0.0

#### Success Criteria
The following methods will be used to validate that the solution is working correctly:
- Automated testing to ensure proper functionality;
- Manual testing to verify user experience and edge cases;
- Load and stress testing, if necessary;
- Monitoring and alerting mechanisms should be established to ensure that the project does not negatively impact performance and reliability.

### Risks
The following risks might be introduced by this set of changes:
- Compatibility issues with Mpesa (some major update on Mpesa side);
- Security vulnerabilities related to handling financial transactions.

Are there any backwards-incompatible changes?
Care should be taken to ensure that the changes are compatible with existing systems and do not break any existing functionality.

Does this project have special implications for security and data privacy?
Any special considerations related to security and data privacy should be addressed and mitigated.

Utilize security mechanisms such as data encryption, such as JWT (JSON Web Token), and enforce transaction limitations.
Could this change significantly increase load on any of our backend systems?
The impact on backend systems, including performance and scalability, should be evaluated and addressed.

### Tools to implement a solution?
The main tools to implement will be:
- Django-ninja or Golang
- Digital Ocean
- AWS
