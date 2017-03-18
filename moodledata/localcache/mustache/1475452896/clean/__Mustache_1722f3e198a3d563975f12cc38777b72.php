<?php

class __Mustache_1722f3e198a3d563975f12cc38777b72 extends Mustache_Template
{
    private $lambdaHelper;

    public function renderInternal(Mustache_Context $context, $indent = '')
    {
        $this->lambdaHelper = new Mustache_LambdaHelper($this->mustache, $context);
        $buffer = '';
        $newContext = array();

        $buffer .= $indent . '<div data-region="grading-navigation-panel" data-first-userid="';
        $value = $this->resolveValue($context->find('userid'), $context);
        $buffer .= call_user_func($this->mustache->getEscape(), $value);
        $buffer .= '" data-courseid="';
        $value = $this->resolveValue($context->find('courseid'), $context);
        $buffer .= call_user_func($this->mustache->getEscape(), $value);
        $buffer .= '" data-showuseridentity="';
        $value = $this->resolveValue($context->find('showuseridentity'), $context);
        $buffer .= call_user_func($this->mustache->getEscape(), $value);
        $buffer .= '">
';
        if ($partial = $this->mustache->loadPartial('mod_assign/grading_navigation')) {
            $buffer .= $partial->renderInternal($context);
        }
        $buffer .= $indent . '</div>
';
        $buffer .= $indent . '<div data-region="grade-panel" ';
        // 'showreview' inverted section
        $value = $context->find('showreview');
        if (empty($value)) {
            
            $buffer .= 'class="fullwidth"';
        }
        $buffer .= '>
';
        $buffer .= $indent . '<div data-region="grade" data-contextid="';
        $value = $this->resolveValue($context->find('contextid'), $context);
        $buffer .= call_user_func($this->mustache->getEscape(), $value);
        $buffer .= '" data-assignmentid="';
        $value = $this->resolveValue($context->find('assignmentid'), $context);
        $buffer .= call_user_func($this->mustache->getEscape(), $value);
        $buffer .= '">
';
        if ($partial = $this->mustache->loadPartial('mod_assign/grading_panel')) {
            $buffer .= $partial->renderInternal($context);
        }
        $buffer .= $indent . '</div>
';
        $buffer .= $indent . '</div>
';
        // 'showreview' section
        $value = $context->find('showreview');
        $buffer .= $this->section945d94a9e062f2a514ab4c9a99887ce3($context, $indent, $value);
        $buffer .= $indent . '<div data-region="grade-actions-panel">
';
        $buffer .= $indent . '<div data-region="grade-actions">
';
        if ($partial = $this->mustache->loadPartial('mod_assign/grading_actions')) {
            $buffer .= $partial->renderInternal($context);
        }
        $buffer .= $indent . '</div>
';
        $buffer .= $indent . '</div>
';
        $buffer .= $indent . '<div data-region="overlay" class="moodle-has-zindex">
';
        if ($partial = $this->mustache->loadPartial('mod_assign/grading_save_in_progress')) {
            $buffer .= $partial->renderInternal($context);
        }
        $buffer .= $indent . '</div>
';

        return $buffer;
    }

    private function section945d94a9e062f2a514ab4c9a99887ce3(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
<div data-region="review-panel">
<div data-region="review">
{{> mod_assign/review_panel }}
</div>
</div>
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
                
                $buffer .= $indent . '<div data-region="review-panel">
';
                $buffer .= $indent . '<div data-region="review">
';
                if ($partial = $this->mustache->loadPartial('mod_assign/review_panel')) {
                    $buffer .= $partial->renderInternal($context);
                }
                $buffer .= $indent . '</div>
';
                $buffer .= $indent . '</div>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

}
