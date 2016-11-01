<?php

class __Mustache_13e9589f98e9c05006c41a6341402d5d extends Mustache_Template
{
    private $lambdaHelper;

    public function renderInternal(Mustache_Context $context, $indent = '')
    {
        $this->lambdaHelper = new Mustache_LambdaHelper($this->mustache, $context);
        $buffer = '';
        $newContext = array();

        $buffer .= $indent . '<ul class="tag_feed media-list">
';
        // 'items' section
        $value = $context->find('items');
        $buffer .= $this->section634bb8035fc55d5b71552b021c48f0a9($context, $indent, $value);
        $buffer .= $indent . '</ul>
';

        return $buffer;
    }

    private function sectionD8335e951715102ddb2365ddac53306b(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
                <div class="itemimage">
                    {{{img}}}
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
                
                $buffer .= $indent . '                <div class="itemimage">
';
                $buffer .= $indent . '                    ';
                $value = $this->resolveValue($context->find('img'), $context);
                $buffer .= $value;
                $buffer .= '
';
                $buffer .= $indent . '                </div>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section578ee03c1441510f95220cbe6ade312c(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
                    <div class="media-heading">
                        {{{heading}}}
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
                
                $buffer .= $indent . '                    <div class="media-heading">
';
                $buffer .= $indent . '                        ';
                $value = $this->resolveValue($context->find('heading'), $context);
                $buffer .= $value;
                $buffer .= '
';
                $buffer .= $indent . '                    </div>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section7ff83aac559d11ff7ec5a8b98e28c695(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
                    <div class="muted">
                        {{{details}}}
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
                
                $buffer .= $indent . '                    <div class="muted">
';
                $buffer .= $indent . '                        ';
                $value = $this->resolveValue($context->find('details'), $context);
                $buffer .= $value;
                $buffer .= '
';
                $buffer .= $indent . '                    </div>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section634bb8035fc55d5b71552b021c48f0a9(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
        <li class="media">
            {{#img}}
                <div class="itemimage">
                    {{{img}}}
                </div>
            {{/img}}
            <div class="media-body">
                {{#heading}}
                    <div class="media-heading">
                        {{{heading}}}
                    </div>
                {{/heading}}
                {{#details}}
                    <div class="muted">
                        {{{details}}}
                    </div>
                {{/details}}
            </div>
        </li>
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
                
                $buffer .= $indent . '        <li class="media">
';
                // 'img' section
                $value = $context->find('img');
                $buffer .= $this->sectionD8335e951715102ddb2365ddac53306b($context, $indent, $value);
                $buffer .= $indent . '            <div class="media-body">
';
                // 'heading' section
                $value = $context->find('heading');
                $buffer .= $this->section578ee03c1441510f95220cbe6ade312c($context, $indent, $value);
                // 'details' section
                $value = $context->find('details');
                $buffer .= $this->section7ff83aac559d11ff7ec5a8b98e28c695($context, $indent, $value);
                $buffer .= $indent . '            </div>
';
                $buffer .= $indent . '        </li>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

}
