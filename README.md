# Susy-Avalia

Plugin para avaliação de código escrito em linguagem C, para ser integrado ao sistema SuSy. A avaliação feita pelo software é conhecida por análise estática, e é utilizada para dar feedback ao desenvolvedor sobre possíveis problemas em seu código, tais como vazamento de memória, acesso à posições inválidas de ponteiros e vetores, etc. Este feedback é importante para qualquer nível de programador, desde iniciantes até programadores experientes dado à vasta cobertura da análise.

## Visão geral

```
project
    |- assets/                                # imagens de exemplo de execuço
    |
    |- latex_documentation_errors/            # 
    |
    |- script/                                # documentos do projeto
    |
    |- susy-avalia-config                     # todos os resultados das análises
    |  |- cppcheck-cfg/                       # gráficos, geralmente as figuras do manuscrito
    |
    |- tests/   
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
cd <your-directory>/project/tests/
```

```
pytest <your-test>.py
```

![Exemplo PyTest](https://github.com/ajcancado/susy-evaluate/blob/master/assets/img_bdd_example.png)

## Licenças

### PyTest

The MIT License (MIT)

Copyright (c) 2004-2017 Holger Krekel and others

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### CppCheck

[GPLv3] (https://www.gnu.org/licenses/gpl-3.0.en.html) - GNU General Public License version 3.0

## Alunos

* **Arthur J. Cançado**
* **Felipe R. Jensen**
* **Gabriell Orisaka**
* **Juliana L. G. Corá**
* **Silvana Trindade**
* **Yusseli L. M. Mendoza**
