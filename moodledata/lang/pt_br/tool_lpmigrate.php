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
 * Strings for component 'tool_lpmigrate', language 'pt_br', branch 'MOODLE_31_STABLE'
 *
 * @package   tool_lpmigrate
 * @copyright 1999 onwards Martin Dougiamas  {@link http://moodle.com}
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

defined('MOODLE_INTERNAL') || die();

$string['coursecompetencymigrations'] = 'Migração de competência do curso';
$string['coursemodulecompetencymigrations'] = 'Migração de recursos de competência e atividades do curso';
$string['errorcouldnotmapcompetenciesinframework'] = 'Não foi possível mapear para nenhuma competência nessa estrutura.';
$string['errorwhilemigratingcoursecompetencywithexception'] = 'Erro ao migrar a competência do curso: {$a}.';
$string['errorwhilemigratingmodulecompetencywithexception'] = 'Erro ao migrar a atividade ou recurso da competência: {$a}';
$string['explanation'] = 'Essa ferramenta pode ser usada para atualizar uma estrutura de competência para uma versão mais recente. Ela procura competências em cursos e atividades usando a estrutura mais antiga, e atualiza os links para apontar para a nova estrutura.

Não é recomendado editar o antigo conjunto de competências diretamente, pois isso mudaria todas as competências que já foram concedidas nos planos de aprendizagem dos usuários.

Normalmente, você importaria a nova versão de uma estrutura, ocultaria a estrutura antiga, e usaria essa ferramenta para migrar novos cursos para a nova estrutura.';
$string['findingcoursecompetencies'] = 'Encontrando competências do curso';
$string['findingmodulecompetencies'] = 'Encontrando atividades e recursos de competências';
$string['lpmigrate:frameworksmigrate'] = 'Migrar estruturas';
$string['migrateframeworks'] = 'Migrar estruturas';
$string['pluginname'] = 'Ferramenta de migração de competências';
$string['warningcouldnotremovecoursecompetency'] = 'A competência do curso não pode ser removida.';
$string['warningcouldnotremovemodulecompetency'] = 'A atividade ou o recurso da competência não pode ser removida.';
$string['warningdestinationcoursecompetencyalreadyexists'] = 'O destino da competência do curso já existe.';
$string['warningdestinationmodulecompetencyalreadyexists'] = 'O destino da atividade ou recurso da competência já existe.';
