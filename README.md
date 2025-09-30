# IBM-RXN

#Live LINK : https://ibm-rxn-physics-chemistry-protocol-extractor.streamlit.app/


##flowchart TD
```mermaid

    A[Start] --> B[Home Page]
    B --> C[Extractor Page]
    C --> D{Paste Reaction Text?}
    D -- Yes --> E[Click Extract Protocol Steps]
    E --> F[IBM RXN API Parsing]
    F --> G[Display Step-by-Step Actions]
    D -- No --> H[Show Warning: Please enter text]
    B --> I[Documentation Page]
    B --> J[About Page]
    B --> K[Contact Page]
    B --> L[Settings Page]
    G --> M[End]
```
