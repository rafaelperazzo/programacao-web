<?php

class __Mustache_67772b4c3f6ee7c1e88333cdb680ee5b extends Mustache_Template
{
    private $lambdaHelper;

    public function renderInternal(Mustache_Context $context, $indent = '')
    {
        $this->lambdaHelper = new Mustache_LambdaHelper($this->mustache, $context);
        $buffer = '';
        $newContext = array();

        $buffer .= $indent . '<form data-region="grading-actions-form" class="hide">
';
        $buffer .= $indent . '    <label>';
        // 'str' section
        $value = $context->find('str');
        $buffer .= $this->sectionE4bbab7d2adabb93d1d7bc2bc143a83a($context, $indent, $value);
        $buffer .= '
';
        $buffer .= $indent . '           <input type="checkbox" name="sendstudentnotifications"
';
        $buffer .= $indent . '                  ';
        // 'defaultsendnotifications' section
        $value = $context->find('defaultsendnotifications');
        $buffer .= $this->sectionE6c044fe8710d3502dd5cb9686c32f3f($context, $indent, $value);
        $buffer .= ' />
';
        $buffer .= $indent . '    </label>
';
        $buffer .= $indent . '    <button type="submit" class="btn btn-primary" name="savechanges">';
        // 'str' section
        $value = $context->find('str');
        $buffer .= $this->sectionCc896fb1429559fad42f2607525c3e3c($context, $indent, $value);
        $buffer .= '</button>
';
        $buffer .= $indent . '    <button type="submit" class="btn" name="resetbutton">';
        // 'str' section
        $value = $context->find('str');
        $buffer .= $this->section65bdb401750b97914f5899115f865e4d($context, $indent, $value);
        $buffer .= '</button>
';
        $buffer .= $indent . '</form>
';
        // 'js' section
        $value = $context->find('js');
        $buffer .= $this->section2c4c4236766022056ffb68d257e30435($context, $indent, $value);

        return $buffer;
    }

    private function sectionE4bbab7d2adabb93d1d7bc2bc143a83a(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = 'sendstudentnotifications, mod_assign';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= 'sendstudentnotifications, mod_assign';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function sectionE6c044fe8710d3502dd5cb9686c32f3f(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = 'checked="checked"';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= 'checked="checked"';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function sectionCc896fb1429559fad42f2607525c3e3c(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = 'savechanges';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= 'savechanges';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section65bdb401750b97914f5899115f865e4d(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = 'reset';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= 'reset';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section2c4c4236766022056ffb68d257e30435(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
require([\'mod_assign/grading_actions\'], function(GradingActions) {
    new GradingActions(\'[data-region="grade-actions"]\');
});
';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= $indent . 'require([\'mod_assign/grading_actions\'], function(GradingActions) {
';
                $buffer .= $indent . '    new GradingActions(\'[data-region="grade-actions"]\');
';
                $buffer .= $indent . '});
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

}
