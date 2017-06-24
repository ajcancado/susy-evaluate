#!/usr/bin/env python3

import os
import subprocess

errors = {
	'uninitialized_variable': {
		'uninitdata': {
			'title': 'Uninitialized data',
			'message': 'Memória foi alocada mas não foi inicializada',
			'issue': 'uninitialized data'
		},
		'uninitStructMember': {
			'title': 'Uninitialized Struct Member',
			'message': 'Variável foi criada em uma \'struct\' mas não foi inicializada',
			'issue': 'uninitialized struct member'
		}
	},
	'unused_function_and_variable': {
		'unusedFunction': {
			'title': 'Unused Function',
			'message': 'Função criada mas nunca foi utilizada',
			'issue': 'unused function'
		},
		'unusedVariable': {
			'title': 'Unused Variable',
			'message': 'Variável nunca foi utilizada',
			'issue': 'unused Variable'
		},
		'unusedAllocatedMemory': {
			'title': 'Unused Allocated Memory',
			'message': 'Recursos de memória alocados nunca foram utilizados',
			'issue': 'unused allocated memory'
		},
		'unreadVariable': {
			'title': 'Unread Variable',
			'message': 'Atribuição de valor à variável mas nunca utilizado',
			'issue': 'unread variable'
		},
		'unusedStructMember': {
			'title': 'Unused Struct Member',
			'message': 'Variável foi criada em uma \'struct\' mas não foi utilizada',
			'issue': 'unused struct member'
		},
		'unassignedVariable': {
			'title': 'Unassigned Variable',
			'message': 'Variável não foi atribuída',
			'issue': 'unassigned variable'
		},
		'unusedLabelSwitch': {
			'title': 'Unused Label Switch',
			'message': 'Label não utilizado',
			'issue': 'unused label switch'
		}
	},
	'checking_data_type': {
		'unpreciseMathCall': {
			'title': 'Unprecise Math Call',
			'message': 'Passando valor que pode gerar resultado indefinido',
			'issue': 'unprecise math call'
		},
		'truncLongCastAssignment': {
			'title': 'Truncated Long Cast Assignment',
			'message': 'Resultado inteiro é atribuído a valor longo, podendo ocasionalmente haver perda de informação',
			'issue': 'truncated long cast assignment'
		},
		'truncLongCastReturn': {
			'title': 'Truncated Long Cast Return',
			'message': 'Resultado inteiro é retornado como valor longo, podendo ocasionalmente haver perda de informação',
			'issue': 'truncated long cast return'
		},
		'floatConversionOverflow': {
			'title': 'Float Conversion Overflow',
			'message': 'Overflow de variável do tipo \'float\'',
			'issue': 'float conversion overflow'
		},
		'pointerArithBool': {
			'title': 'Pointer Arith Boolean',
			'message': 'Valor booleano atribuído a ponteiro',
			'issue': 'Pointer Arith Boolean'
		},
		'incorrectStringBooleanError': {
			'title': 'Incorrect String Boolean Error',
			'message': 'Conversão literal de variável tipo carácter para booleano sempre é verdadeiro',
			'issue': 'incorrect string boolean error'
		},
		'bufferAccessOutOfBounds': {
			'title': 'Buffer Access Out Of Bounds',
			'message': 'Vetor acessado em índice inválido, portanto fora do seu limite',
			'issue': 'buffer access out Of bounds'
		},
		'outOfBounds': {
			'title': 'Out Of Bounds',
			'message': 'Acesso inválido',
			'issue': 'out of bounds'
		},
		'pointerOutOfBounds': {
			'title': 'Pointer Out Of Bounds',
			'message': 'Acesso a posição inválida do ponteiro',
			'issue': 'pointer out of bounds'
		},
		'possileBufferAccessOutBounds': {
			'title': 'Possile Buffer Access Out Bounds',
			'message': 'Possível acesso inválido',
			'issue': 'possile buffer access out bounds'
		}
	},
	'syntax_suspected': {
		'clarifyCondition': {
			'title': 'Clarify Condition',
			'message': 'Condição não está claramente definida',
			'issue': 'clarify condition'
		},
		'compareBoolExpressionWithInt': {
			'title': 'Compare Bool Expression with Integer',
			'message': 'Comparação de tipo booleano com tipo inteiro',
			'issue': 'compare boolen expression with integer'
		}
	},
	'format_string': {
		'wrongPrintScanfArgNum': {
			'title': 'Wrong Print Scanf Argument Number',
			'message': 'Número de variáveis utilizadas não corresponde com o número de formatadores',
			'issue': 'wrong print scanf argument number'
		},
		'invalidScanfArgType_s': {
			'title': 'Invalid Scanf Argument Type String',
			'message': 'Scanf com argumento do tipo \'string/char*\' inválido',
			'issue': 'invalid scanf argument type string'
		},
		'invalidScanfArgType_int': {
			'title': 'Invalid Scanf Argument Type Integer',
			'message': 'Scanf com argumento do tipo \'int\' inválido',
			'issue': 'invalid scanf argument type integer'
		},
		'invalidScanfArgType_float': {
			'title': 'Invalid Scanf Argument Type Float',
			'message': 'Scanf com argumento do tipo \'float\' inválido',
			'issue': 'invalid scanf argument type float'
		},
		'invalidPrintfArgType_s': {
			'title': 'Invalid Print Argument Type String',
			'message': 'Argumento do tipo \'string/char*\' no formato apresentado é inválido',
			'issue': 'invalid print argument type string'
		},
		'invalidPrintArgType_n': {
			'title': 'Invalid Print Argument Type Number',
			'message': 'Argumento do tipo \'number\' no formato apresentado é inválido',
			'issue': 'invalid print argument type number'
		},
		'invalidPrintArgType_p': {
			'title': 'Invalid Print Argument Type Pointer',
			'message': 'Argumento do tipo ponteiro no formato apresentado é inválido',
			'issue': 'invalid print argument type pointer'
		},
		'invalidPrintArgType_int': {
			'title': 'Invalid Print Argument Type Integer',
			'message': 'Argumento de tipo \'int\' é inválido neste caso',
			'issue': 'invalid print argument type integer'
		},
		'invalidPrintArgType_uint': {
			'title': 'Invalid Print Argument Type Usigned Integer',
			'message': 'Argumento de tipo \'unsigned int\' é inválido neste caso',
			'issue': 'invalid print argument type usigned integer'
		},
		'invalidPrintArgType_sint': {
			'title': 'Invalid Print Argument Type Small Integer',
			'message': 'Argumento de tipo \'short int\' é inválido neste caso',
			'issue': 'invalid print argument type small integer'
		},
		'invalidPrintArgType_float': {
			'title': 'Invalid Print Argument Type Float',
			'message': 'Argumento de tipo \'float\' é inválido neste caso',
			'issue': 'invalid print argument type float'
		},
		'invalidLengthModifierError': {
			'title': 'Invalid Length Modifier Error',
			'message': 'Formato de \'string/char*\' modificado não pode ser utilizado sem conversão específica',
			'issue': 'invalid length modifier error'
		},
		'invalidScanfFormatWidth': {
			'title': 'Invalid Scanf Format Width',
			'message': 'Tamanho da variável no formato \'string/char*\' é inválida',
			'issue': 'invalid scanf format width'
		},
		'wrongPrintfScanfParameterPositionError': {
			'title': 'Wrong Printf Scanf Parameter Position Error',
			'message': 'Referenciamento de parâmetro foi realizado incorretamente',
			'issue': 'wrong printf scanf parameter position error'
		},
	},
	'memory_leak': {
		'resourceLeak': {
			'title': 'Resource Leak',
			'message': 'Vazamento de recursos',
			'issue': 'resource leak'
		},
		'deallocDealloc': {
			'title': 'Dealloc Dealloc',
			'message': 'Ponteiro foi liberado duas vezes',
			'issue': 'dealloc dealloc'
		},
		'deallocuse': {
			'title': 'Dealloc Use',
			'message': 'Acesso a variável já desalocada',
			'issue': 'dealloc use'
		},
		'mismatchAllocDealloc': {
			'title': 'Mismatch Allocation and Deallocation',
			'message': 'Falta de alocação ou desalocação de memória',
			'issue': 'mismatch allocation and deallocation'
		},
		'memleakOnRealloc': {
			'title': 'Memleak On Realloc',
			'message': 'Vazamento de memória no processo de realocação',
			'issue': 'memleak on realloc'
		},
		'doubleFree': {
			'title': 'Double Free',
			'message': 'Ponteiro foi liberado duas vezes',
			'issue': 'double free'
		},
		'deallocret': {
			'title': 'Dealloc Return error',
			'message': 'Retorno/acesso de variável já desalocada',
			'issue': 'dealloc return error'
		},
	},
	'null_pointer': {
		'nullPointerDefaultArg': {
			'title': 'Null Pointer Default Argument',
			'message': 'Possível acesso a pointeiro nulo se o valor padrão foi utilizado',
			'issue': 'null pointer default argument'
		},
		'nullPointerRedundantCheck': {
			'title': 'Null Pointer Redundant Check',
			'message': 'Existe uma possibilidade do valor acessado do ponteiro ser nulo',
			'issue': 'null pointer redundant check'
		},
		'nullPointerArithmetic': {
			'title': 'Null Pointer Arithmetic',
			'message': 'Overflow na aritmética de ponteiro, ponteiro nulo é subtraído',
			'issue': 'null pointer arithmetic'
		}
	},
	'check_file': {
		'writeReadOnlyFile': {
			'title': 'Write Read Only File',
			'message': 'Operação de escrita em um arquivo que foi aberto somente para leitura',
			'issue': 'write read only file'
		},
		'readWriteOnlyFile': {
			'title': 'Read Write Only File',
			'message': 'Operação de leitura em um arquivo que foi aberto somente para escrita',
			'issue': 'read write only file'
		},
		'useClosedFile': {
			'title': 'Use Closed File',
			'message': 'Arquivo utilizado que não foi aberto',
			'issue': 'use closed file'
		},
		'fflushOnInputStream': {
			'title': 'fflush On Input Stream',
			'message': 'Chamada de função fflush() no stream de entrada, podendo resultar em comportamento indefinido em sistemas não-linux',
			'issue': 'fflush on input stream'
		}
	}
}

feature = """Feature: {title}
    Code analysis beyond compilation

Scenario: Code with {issue}
    Given <filename>.c has {issue}
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) {message}"

Scenario: Code without {issue}
    Given <filename>.c doesn't have {issue}
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"
"""

home = '/home/silvana/susy-tests'

for _k, group in errors.items():
	if not os.path.exists(home + '/' + _k):
		os.makedirs(home + '/' + _k)

		for key, error in group.items():
			feature_filename = home + '/' + _k + '/' + key + '.feature'
			test_filename = home + '/' + _k + '/test_' + key + '.py'

			with open(feature_filename, 'w') as file:
				file.write(feature.format(title=error['title'], issue=error['issue'], message=error['message']))

			subprocess.check_output('pytest-bdd generate ' + feature_filename + ' > ' + test_filename, shell=True)

basic_structure = """#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
}
"""

cases_cpp = '/home/silvana/susy-tests/support'

for _k, group in errors.items():
	if not os.path.exists(cases_cpp + '/' + _k):
		os.makedirs(cases_cpp + '/' + _k)

		for key, error in group.items():
			if not os.path.exists(cases_cpp + '/' + _k + '/' + key):
				os.makedirs(cases_cpp + '/' + _k + '/' + key)

				cases = [
					cases_cpp + '/' + _k + '/' + key + '/bad.c',
					cases_cpp + '/' + _k + '/' + key + '/good.c'
				]


				for case in cases:
					with open(case, 'w') as file:
						file.write(basic_structure)
				#for tests
				cases_address = [
					cases_cpp + '/' + 'bad_' + key + '.txt',
					cases_cpp + '/' + 'good_' + key + '.txt'
				]

				for case in cases_address:
					with open(case, 'w') as file:
						if 'bad' in case:
							file.write(cases[0])
						else:
							file.write(cases[1])
