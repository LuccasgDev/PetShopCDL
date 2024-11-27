CREATE DATABASE PetStoreDb;

USE PetStoreDb;

-- Tabela Donos
CREATE TABLE Donos (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    CPF VARCHAR(11) NULL, -- Permite valores nulos para CPF
    Telefone VARCHAR(11) NULL -- Permite valores nulos para Telefone
);

-- Tabela Animais
CREATE TABLE Animais (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    Idade INT NOT NULL,
    Peso DOUBLE NOT NULL,
    Observacao TEXT,
    Especie VARCHAR(255) DEFAULT 'Desconhecida', -- Coluna Especie com valor padrão
    DonoId INT,
    FOREIGN KEY (DonoId) REFERENCES Donos(Id) ON DELETE CASCADE
);

-- Tabela Consultas
CREATE TABLE Consultas (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    AnimalId INT,
    DataConsulta DATE NOT NULL,
    Descricao TEXT,
    FOREIGN KEY (AnimalId) REFERENCES Animais(Id) ON DELETE CASCADE
);

-- Exemplo de consulta para ver todos os donos e animais
SELECT * FROM Donos;
SELECT * FROM Animais;
SELECT * FROM Consultas;
DESCRIBE Animais;

INSERT INTO Donos (Nome, Email, CPF, Telefone) 
VALUES ('Carlos Silva', 'carlos@email.com', '12345678900', '85999999999');


DESCRIBE animais;
DESCRIBE consultas;

INSERT INTO Animais (Nome, Tipo, Idade, Peso, Observacao, especie, DonoId) 
VALUES ('Rodolf', 'Cao', '5', '8','obeso', 'pasto Alemao', '3');


SELECT id, nome, tipo, idade, peso, especie FROM animais;
