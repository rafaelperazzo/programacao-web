<?php

class __Mustache_f6ecb01a635df99f7e819e2f5828ff5f extends Mustache_Template
{
    public function renderInternal(Mustache_Context $context, $indent = '')
    {
        $buffer = '';
        $newContext = array();

        $value = $this->resolveValue($context->find('subject'), $context);
        $buffer .= $indent . $value;
        $buffer .= '
';

        return $buffer;
    }
}
