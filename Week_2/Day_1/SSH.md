# Understanding SSH (Secure Shell)

## What is SSH? What is it used for?

SSH  stands for Secure Shell, it is a cryptographic network protocol used for securely accessing and managing network services over an unsecured network. It provides a secure channel for communication between two computers, typically a client and a server. SSH is widely used for various purposes, including:

1. **Remote Access**: SSH allows users to access a remote computer or server securely. This is most commonly used for remote system access.

2. **File Transfer**: It enables secure file transfers between computers. 

3. **Tunneling**: SSH can create encrypted tunnels to forward network connections, providing a secure way to access services on a remote network.

## How does SSH work? What are Private and Public keys?

SSH operates using a pair of cryptographic keys: a **private key** and a **public key**:

- **Private Key**: The private key is kept secret on the client-side (your computer). It's used for decrypting data that was encrypted with the corresponding public key.

- **Public Key**: The public key is placed on the server you want to access securely. It's used to encrypt data that can only be decrypted by the private key. This setup ensures that even if someone gains access to the public key, they can't reverse-engineer it to obtain the private key.

The process of authentication involves the following steps:

1. The client initiates a connection to the server and provides its public key.

2. The server checks if the client's public key is authorized to access the system.

3. If authorized, the server uses the client's public key to encrypt a message, which the client decrypts with its private key to prove its identity.

## Why use SSH? How does it increase security?

- **Encryption**: All data exchanged between the client and server is encrypted, preventing eavesdropping and data interception.

- **Authentication**: The use of key pairs ensures that only authorized users can access the system. Passwords are not sent over the network, reducing the risk of password-based attacks.

- **Data Integrity**: SSH ensures that the data sent and received has not been tampered with during transmission.

- **Port Forwarding**: SSH can be used to create secure tunnels for other protocols, adding an extra layer of security for services.

## How can you create an SSH key pair?
1. Open a terminal or command prompt on your local computer.

2. Use the `ssh-keygen` command to generate a key pair. For example:

   ```bash
   ssh-keygen -t rsa -b 2048
   ```
This command generates an RSA key pair with a bit length of 2048.

1. You will be prompted to choose a location to save the key pair.

2. You can also set a passphrase to further secure your private key. This passphrase adds an extra layer of protection.

3. You will now have a private key (typically named id_rsa) and a public key (typically named id_rsa.pub).
