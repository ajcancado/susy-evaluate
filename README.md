# Susy-Avalia

Plugin para avaliação de código escrito em linguagem C, para ser integrado ao sistema SuSy. A avaliação feita pelo software é conhecida por análise estática, e é utilizada para dar feedback ao desenvolvedor sobre possíveis problemas em seu código, tais como vazamento de memória, acesso à posições inválidas de ponteiros e vetores, etc. Este feedback é importante para qualquer nível de programador, desde iniciantes até programadores experientes dado à vasta cobertura da análise.

## Visão geral

```
project
    |- assets/                                # imagens de exemplo de execução
    |
    |- latex_documentation_errors/            # 
    |
    |- script/                                # documentos do projeto
    |
    |- susy-avalia-config                     # 
    |  |- cppcheck-cfg/                       # 
    |
    |- tests/                                 #
    |  |- check_file/                         #
    |  |- checking_data_type/                 #
    |  |- format_string/                      #
    |  |- memory_leak/                        #
    |  |- null_pointer/                       #
    |  |- support/                            #
    |  |- syntax_suspected/                   #
    |  |- uninitialized_variable/             #
    |  |- unused_function_and_variable/       #
    |
    |- AUTHORS                                # atores do projeto
    |- LICENCE                                # licença de uso
    |- README                                 # descrição do conteúdo do diretório do projeto
    |- documentacao_mensagens_de_erro.pdf     # 
    |- susy-avalia.py                         # script de execução do susy-avalia
```

## Ferramentas

### [PyTest](https://docs.pytest.org/en/latest/)

O PyTest facilita a criação de pequenos testes a testes funcionais complexos para aplicações e bibliotecas.

### [CppCheck](http://cppcheck.sourceforge.net/)

Cppcheck é uma ferramenta de anális estática de codigo para C/C++ . Diferente dos compiladores C/C++ e outras ferramentas de análise que não detectão erros de sintaxe no código. Cppcheck primeiramente detecta os tipos de "bugs" que não so detectados normalmente. O objetivo é detectar apenas erros reais, buscando não ter falsos positivos.

## Instalação

### PyTest

```
pip install -U pytest
```

* Deve-se ter instalado na máquina o Python, de preferência a versão 3.

### CppCheck

```
<your-package-manager> install cppcheck
```

* Em algumas distribuiço do linux o gerenciador de pacotes pode no conseguir instalar automaticamente, para isso será necessário a instalação no modo HardCode. Mais informações [aqui](http://cppcheck.sourceforge.net/#download).

## Exemplos

### PyTest

```
cd <your-directory>/susy-evaluate/tests/
```

```
pytest <your-test>.py
```

![Exemplo PyTest](https://github.com/ajcancado/susy-evaluate/blob/master/assets/img_bdd_example.png)

### Susy-Avalia

```
cd <your-directory>/susy-avaluate/>
```

```
python3 susy-avalia.py <your-file-to-evaluate.c>
```

ou caso queira especificar o arquivo de saida:

```
python3 susy-avalia.py <your-file-to-evaluate.c> <your-directory/output.txt>
```

![Exemplo Susy-Avalia](https://github.com/ajcancado/susy-evaluate/blob/master/assets/img_susy-avalia_example.png)

## Licenças

### PyTest

Copyright Holger Krekel and others, 2004-2017.

Distributed under the terms of the [MIT](https://github.com/pytest-dev/pytest/blob/master/LICENSE) license, pytest is free and open source software.

### CppCheck

[GNU General Public License version 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

## Alunos

* **Arthur J. Cançado**
* **Felipe R. Jensen**
* **Gabriell Orisaka**
* **Juliana L. G. Corá**
* **Silvana Trindade**
* **Yusseli L. M. Mendoza**
