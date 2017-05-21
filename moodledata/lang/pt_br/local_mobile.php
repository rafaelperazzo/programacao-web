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
 * Strings for component 'local_mobile', language 'pt_br', branch 'MOODLE_31_STABLE'
 *
 * @package   local_mobile
 * @copyright 1999 onwards Martin Dougiamas  {@link http://moodle.com}
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

defined('MOODLE_INTERNAL') || die();

$string['allowpermissions'] = 'Conceder permissões para a função de usuário autenticado';
$string['allowpermissionsdescription'] = 'Editar a função de usuário autenticado e permitir o recurso moodle/webservice:createtoken';
$string['cannotcreatetoken'] = 'A geração automática de tokens não está disponível para os administradores do site (eles devem criar um token manualmente no site)';
$string['checkpluginconfiguration'] = 'Verificar a configuração do plugin';
$string['clickheretolaunchtheapp'] = 'Por favor, clique aqui se o aplicativo não abrir automaticamente';
$string['customlangstrings'] = 'Strings de idiomas personalizadas';
$string['customlangstrings_desc'] = 'As palavras e frases mostradas na aplicação podem ser personalizadas aqui. Digite em cada nova linha a string personalizada do idioma no formato: identificador da string, string personalizada do idioma e código do idioma, separados por uma barra vertical. Por exemplo:
<pre>
mm.user.student|Learner|en
mm.user.student|Aluno|et
</pre>
Para uma lista completa de identificadores de strings consulte <a href="https://github.com/moodlehq/moodlemobile-phonegapbuild/blob/master/build/lang/en.json">esta lista</a>.';
$string['custommenuitems'] = 'Itens de menu personalizados';
$string['custommenuitems_desc'] = 'Itens adicionais podem ser adicionados ao menu principal da aplicação, se os especificar aqui. Digite cada item de menu personalizado em cada nova linha no formato: texto do item, endereço da hiperligação, método de abertura da hiperligação (inappbrowser, browser or embedded) e código de idioma (opcional, para mostrar o item apenas a usuários do idioma especificado), separados por barras verticais. Por exemplo:
<pre>
App\'s help | https://someurl.xyz/help | inappbrowser | en
Visit our SIS | https://someurl.xyz | browser | en
My grades | https://someurl.xyz/local/mygrades/index.php | embedded | en
As minhas notas| https://someurl.xyz/local/mygrades/index.php | embedded | pt
</pre>
Use \'inappbrowser\' quando quiser abrir a hiperligação num navegador sem sair da aplicação, use \'browser\' para abrir a hiperligação no navegador da internet predefinido do dispositivo e \'embedded\' se quiser mostrar a hiperligação incorporada numa nova página na aplicação.';
$string['disabledfeatures'] = 'Recursos desativados';
$string['disabledfeatures_desc'] = 'Selecione aqui os recursos que deseja desativar no aplicativo para dispositivos móveis do seu site. Observe que alguns recursos listados aqui podem estar desativados por meio de outras configurações do site. Você terá que sair e entrar novamente no aplicativo para ver as alterações.';
$string['enableadditionalservice'] = 'Ativar o serviço de recursos adicionais do Moodle Mobile';
$string['enableadditionalservicedescription'] = 'Esse serviço deve estar ativado.';
$string['forcelogout'] = 'Forçar saída';
$string['forcelogout_desc'] = 'Se ativar esta escolha, a opção da aplicação \'Alterar site\' é substituída por \'Terminar sessão\'. Isto resulta que o usuário fique completamente desligado. É necessário voltar a inserir a sua senha na próxima vez que pretenderem acessar ao site.';
$string['local_mobiledescription'] = 'Plugin que estende os recursos do serviço móvel';
$string['local_mobilesettings'] = 'Configurações';
$string['local_mobiletypeoflogin'] = 'Escolha o tipo de login';
$string['local_mobiletypeoflogin_key'] = 'Tipo de login';
$string['local_mobileurlscheme'] = 'Utilize esta configuração para forçar o URL scheme para o login através de uma janela do navegador. Na maioria dos casos, deve ficar vazio.';
$string['local_mobileurlscheme_key'] = 'URL scheme';
$string['loginintheapp'] = 'Através do aplicativo';
$string['logininthebrowser'] = 'Através de uma janela do navegador (para plugins SSO)';
$string['loginintheinappbrowser'] = 'Através de um navegador embutido (para plugins SSO)';
$string['mainmenu'] = 'Menu principal';
$string['mobilefeatures'] = 'Recursos móveis';
$string['pluginname'] = 'Funcionalidades adicionais do Moodle Mobile';
$string['pluginnotenabledorconfigured'] = 'O plugin local do Moodle Mobile deve ser ativado e configurado para iniciar o aplicativo';
$string['remoteaddons'] = 'Complementos remotos';
