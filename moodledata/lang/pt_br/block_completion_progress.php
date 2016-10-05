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
 * Strings for component 'block_completion_progress', language 'pt_br', branch 'MOODLE_31_STABLE'
 *
 * @package   block_completion_progress
 * @copyright 1999 onwards Martin Dougiamas  {@link http://moodle.com}
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

defined('MOODLE_INTERNAL') || die();

$string['completed_colour'] = '#73A839';
$string['completed_colour_descr'] = 'Código de cores HTML para elementos que foram concluídos';
$string['completed_colour_title'] = 'Cor concluída';
$string['completion_not_enabled'] = 'Rastreamento de conclusão não está habilitado neste site.';
$string['completion_not_enabled_course'] = 'Rastreamento de conclusão não está habilitado neste curso.';
$string['completion_progress:addinstance'] = 'Adicionar um novo bloco de Progresso de Conclusão';
$string['completion_progress:myaddinstance'] = 'Adicionar um bloco de Progresso de Conclusão à minha página inicial';
$string['completion_progress:overview'] = 'Visualizar visão geral do curso de Progresso de Conclusão para todos os alunos';
$string['completion_progress:showbar'] = 'Mostrar a barra no bloco de Progresso de Conclusão';
$string['config_activitiesincluded'] = 'Atividades incluídas';
$string['config_activitycompletion'] = 'Todas as atividades com conjunto de conclusão';
$string['config_default_title'] = 'Progresso de Conclusão';
$string['config_group'] = 'Disponível apenas ao grupo';
$string['config_header_monitored'] = 'Monitorado';
$string['config_icons'] = 'Usar ícones na barra';
$string['config_longbars'] = 'Como apresentar barras grandes';
$string['config_orderby'] = 'Ordenar barra por';
$string['config_orderby_course_order'] = 'Ordenando no curso';
$string['config_orderby_due_time'] = 'Hora usando "{$a}" data';
$string['config_percentage'] = 'Mostrar porcentagem aos alunos';
$string['config_scroll'] = 'Rolagem';
$string['config_selectactivities'] = 'Selecionar atividades';
$string['config_selectedactivities'] = 'Atividades selecionadas';
$string['config_squeeze'] = 'Compressão';
$string['config_title'] = 'Alternar título';
$string['coursenametoshow'] = 'Nome do curso para mostrar no Painel de Instrumentos';
$string['defaultlongbars'] = 'Apresentação padrão para barras grandes';
$string['fullname'] = 'Nome do curso completo';
$string['futureNotCompleted_colour'] = '#025187';
$string['futureNotCompleted_colour_descr'] = 'Código de cor HTML para elementos futuros que ainda não foram concluídos';
$string['futureNotCompleted_colour_title'] = 'Cor não-concluída de futuro';
$string['how_activitiesincluded_works'] = 'Como inclusão de atividades funciona';
$string['how_activitiesincluded_works_help'] = '<p>Por padrão, todas as atividades com conjunto de configurações de conclusão de Atividade são incluídas na barra.</p><p>Você pode também selecionar manualmente atividades que serão incluídas.</p>';
$string['how_group_works'] = 'Como grupo disponível funciona';
$string['how_group_works_help'] = '<p>Selecionando um grupo limitará a exibição desse bloco para esse grupo apenas.</p>';
$string['how_longbars_works'] = 'Como barras grandes são apresentadas';
$string['how_ordering_works'] = 'Como ordenação funciona';
$string['how_ordering_works_help'] = '<p>Existem duas maneiras de ordenar atividades no bloco de Progresso de Conclusão.</p><ul><li><em>Hora usando "Conclusão prevista em" data</em> (default)<br />As datas de conclusão prevista de atividades/recursos são usadas para ordenar a barra. Onde atividades/recursos não possuem uma data de conclusão prevista date, ordenação no curso é utilizada. Quando essa opção é utilizada, o indicador AGORA é mostrado.</li><li><em>Ordenação no curso</em><br />Atividades/recursos são apresentados na mesma ordem em que estão na página do curso. Quando essa opção é usada, datas de conclusão prevista são ignoradas. Quando essa opção é utilizada, o indicador AGORA não é mostrado.</li></ul>';
$string['how_selectactivities_works'] = 'Como inclusão de atividades funciona';
$string['how_selectactivities_works_help'] = '<p>Para selecionar atividades que serão incluídas na barra manualmente, certifique-se de que "Atividades Incluídas" está configurada para "atividades selecionadas".</p><p>Apenas atividades com configurações de conclusão de atividade armazenadas podem ser incluídas.</p><p>Pressione a tecla CTRL para selecionar múltiplas atividades.</p>';
$string['lastonline'] = 'Último no curso';
$string['mouse_over_prompt'] = 'Posicione o mouse sobre ou toque a barra para informações.';
$string['no_activities_config_message'] = 'Não existem atividades ou recursos com conclusão de atividade armazenada ou nenhuma atividade ou recurso foi selecionado. Armazene conclusão de atividade em atividades e recursos, em seguida configure esse bloco.';
$string['no_activities_message'] = 'Nenhuma atividade ou recurso está sendo monitorado. Use config para configurar o monitoramento.';
$string['no_blocks'] = 'Nenhum bloco de Progresso de Conclusão está configurado para seus cursos.';
$string['no_courses'] = 'Você não está inscrito em nenhum curso. Apenas barras de cursos inscritos serão mostradas.';
$string['not_all_expected_set'] = 'Nem todas as atividades concluídas possuem uma "{$a}" data armazenada.';
$string['notCompleted_colour'] = '#C71C22';
$string['notCompleted_colour_descr'] = 'Código de cor HTML para elementos atuais que ainda não foram concluídos';
$string['notCompleted_colour_title'] = 'Cor não-concluída';
$string['no_visible_activities_message'] = 'Nenhuma das atividades monitoradas está atualmente disponível';
$string['now_indicator'] = 'AGORA';
$string['overview'] = 'Visão geral de alunos';
$string['pluginname'] = 'Progresso de Conclusão';
$string['progress'] = 'Progresso';
$string['progressbar'] = 'Progresso de Conclusão';
$string['showallinfo'] = 'Mostrar todas as informações';
$string['showinactive'] = 'Mostrar alunos inativos em Visão Geral';
$string['submitted'] = 'Submetido';
$string['submittednotcomplete_colour'] = '#FFCC00';
$string['submittednotcomplete_colour_descr'] = 'Código de cor HTML para elementos que foram submetidos, mas ainda não estão concluídos';
$string['time_expected'] = 'Previsto';
$string['why_set_the_title'] = 'Por que você pode querer definir o título da instância do bloco?';
$string['why_set_the_title_help'] = '<p> Pode haver várias instâncias do bloco de Progresso de Conclusão. Você pode usar diferentes blocos de Progresso de Conclusão para monitorar diferentes conjuntos de atividades ou recursos. Por exemplo, você pode acompanhar o progresso nas atribuições em um bloco e questionários em outro. Por esta razão, você pode substituir o título padrão e definir um título de bloco mais apropriado para cada caso. </p>';
$string['why_show_precentage'] = 'Por que mostrar uma porcentagem de progresso aos alunos?';
$string['why_show_precentage_help'] = '<p>É possível mostrar uma percentagem global de progresso para os alunos. </p> <p>Este valor é calculado como o número de atividades concluídas dividido pelo número total de atividades na barra.</p> <p>A porcentagem de progresso aparece até o aluno posicionar o mouse sobre um item na barra.</p>';
$string['why_use_icons'] = 'Por que você pode querer usar ícones?';
$string['why_use_icons_help'] = '<p>Você pode querer adicionar ícones tick e cross no Progresso de Conclusão para fazer este bloco visualmente mais acessível para alunos com daltonismo.</p><p> Pode também fazer o significado do bloco mais claro se você acredita que as cores não são intuitivas, seja por razões culturais ou pessoais.</ p>';
