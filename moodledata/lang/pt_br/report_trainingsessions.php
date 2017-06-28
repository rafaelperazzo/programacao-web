<?php

// This file is part of Moodle - http://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <http://www.gnu.org/licenses/>.

/**
 * Strings for component 'report_trainingsessions', language 'pt_br', branch 'MOODLE_30_STABLE'
 *
 * @package   report_trainingsessions
 * @copyright 1999 onwards Martin Dougiamas  {@link http://moodle.com}
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

defined('MOODLE_INTERNAL') || die();

$string['activitytime'] = 'Tempo em atividades:';
$string['activitytime_help'] = '<p> Este cálculo de tempo considera todo o tempo de uso gasto nas atividades do curso, deixando os tempos de layout do curso fora do cálculo. Em certos casos (quando se usa o Learning Time Check (não padrão) com alocação de tempo padrão (http://github.com/vfremaux/moodle-mod_learningtimecheck.git), tempos padrões adicionais são usados em vez de tempos reais extraídos do log. </ p>';
$string['addmodulelabel'] = 'Adicionar módulo de atividade';
$string['addmoduletitle'] = 'Adicione um módulo de atividade que deseja para adicionar nota no relatório';
$string['advancement'] = 'Avanço';
$string['allcourses'] = 'Todos os cursos';
$string['allgroups'] = 'Todos os grupos';
$string['ashtml'] = 'Formato HTML';
$string['asxls'] = 'Baixar no formato Excel';
$string['authoritysign'] = 'Autoridade de Educação';
$string['batchdate'] = 'Data da tarefa';
$string['batchdate_help'] = '<p> Esta configuração significa a data exata em que o lote será lançado e os documentos gerados. Se você teme que os documentos sejam pesados (muitos estudantes, muitas histórias para rastrear), escolha uma data / hora em um período de baixa carga do seu servidor. </ p>';
$string['batchreports_task'] = 'Relatórios em lote';
$string['bgcolor'] = 'Cor de fundo';
$string['checklistadvice'] = 'Efeitos especiais de conclusão lateral';
$string['chooseagroup'] = 'Escolher um grupo';
$string['chooseaninstitution'] = 'Escolher uma instituição';
$string['colors'] = 'Cores';
$string['columnname'] = 'Nome da coluna:';
$string['connections'] = 'Conexões';
$string['contiguoussessions'] = 'Sessões contíguas';
$string['coupling'] = 'Acoplamento';
$string['course'] = 'Curso';
$string['courseglobals'] = 'Áreas globais do curso';
$string['coursegrade'] = 'Habilitar pontuação do curso';
$string['courselabel'] = 'como coluna:';
$string['coursename'] = 'Nome do grupo';
$string['courseraw'] = 'Lotes';
$string['coursesessions'] = 'Sessões de trabalho em curso (tempos reais adivinhados)';
$string['coursestart'] = 'Data de início do curso';
$string['crop'] = 'Escolher sessões fora de alcance';
$string['csv'] = 'Texto (CSV)';
$string['csvoutputtoiso'] = 'Saída Iso CSV';
$string['csvoutputtoiso_desc'] = 'Se ativado, o relatório bruto do curso será gerado na codificação ISO-8859-1 para aplicativos compatíveis CSV antigos.';
$string['currentcourse'] = 'Curso atual';
$string['disabled'] = '|--------- desativado -----------|';
$string['done'] = 'Realizado:';
$string['duration'] = 'Duração';
$string['elapsed'] = 'Tempo total';
$string['elapsedadvice'] = 'O tempo decorrido pode ser diferente do intervalo de tempo da sessão devido a tempos de crédito adicionais nas quebras de sessões. Consulte a configuração do bloco Usar Estatísticas.';
$string['email'] = 'E-mail';
$string['enablecoursescore'] = 'Ativar pontuação do curso';
$string['enablelearningtimecheckcoupling'] = 'Ativar acoplamento LTC';
$string['enddate'] = 'Data final';
$string['enterprisesign'] = 'Empreendimento';
$string['equlearningtime'] = 'Tempo de treinamento equivalente:';
$string['equlearningtime_help'] = '<p> O tempo de aprendizagem equivalente resume todo o tempo gasto no curso, incluindo os tempos de alocação padrão se o módulo da Lista de Verificação da Verificação do Tempo de Aprendizado for usado (http://github.com/vfremaux/moodle-mod_learningtimecheck.git). </p>';
$string['errorbadcoursestructure'] = 'Erro na estrutura do curso: id incorreto {$a}';
$string['errorbadviewid'] = 'visualização de relatório não existente';
$string['errorcoursetoolarge'] = 'O curso é muito grande. Escolhendo um grupo';
$string['errornotingroup'] = 'Você não tem acesso a todos os usuários e não tem nenhuma associação de grupo.';
$string['extrauserinfo'] = 'Informações adicionais do usuário em relatórios';
$string['extrauserinfo_desc'] = 'Você pode opcionalmente adicionar dados do campo do usuário à parte de informação do usuário';
$string['firstaccess'] = 'Primeiro acesso';
$string['firstconnection'] = 'Primeira conexão';
$string['firstenrolldate'] = 'Primeira matrícula';
$string['firstname'] = 'Primeiro nome';
$string['from'] = 'De';
$string['generatereports'] = 'Gerar relatórios';
$string['generateXLS'] = 'Gerar no formato XLS';
$string['gradesettings'] = 'Configurações de nota';
$string['head1application'] = 'As cores Head 1 são usadas na linha superior do cabeçalho quando apropriadas.';
$string['head2application'] = 'As cores Head 2 são usadas na linha de cabeçalho normal acima das colunas de dados. Este é o caso mais comum.';
$string['headsection'] = 'Seção do título';
$string['hits'] = 'Acessos';
$string['incourses'] = 'Nos cursos';
$string['institution'] = 'Instituição';
$string['institutions'] = 'Instituições';
$string['item'] = 'Item';
$string['nodata'] = 'Não há dados de curso';
$string['nopermissiontoview'] = 'Você não tem permissões suficientes neste curso para ver esta informação.';
$string['over'] = 'sobre';
$string['pluginname'] = 'Sessões de Treinamento';
$string['reports'] = 'Relatórios';
$string['role'] = 'Papel';
$string['sectionname'] = 'Nome da seção';
$string['seedetails'] = 'Veja mais detalhes';
$string['sessionend'] = 'Final da sessão';
$string['sessionreports'] = 'Relatório de sessão de usuário';
$string['sessionstart'] = 'Início da sessão';
$string['startdate'] = 'Data inicial';
$string['timeelapsed'] = 'Tempo gasto';
$string['timeelapsedcurweek'] = 'Tempo gasto semana corrente';
$string['todate'] = 'Data final';
$string['totalduration'] = 'Duração total';
$string['totalsessions'] = 'Tempo total da sessão';
$string['trainingreports'] = 'Relatórios de treinamento';
$string['trainingsessions'] = 'Sessões de Treinamento';
$string['trainingsessions_report_advancement'] = 'Relatório de Progresso';
$string['trainingsessions_report_connections'] = 'Relatório de conexão';
$string['trainingsessions_report_institutions'] = 'Relatório de instituição';
$string['updatefromaccountstart'] = 'Obter do primeiro acesso do usuário';
$string['uploadresult'] = 'Baixar resultados brutos';
$string['user'] = 'Por participante';
$string['weekstartdate'] = 'Início da semana';
$string['workingsessions'] = 'Sessões de trabalho:';
