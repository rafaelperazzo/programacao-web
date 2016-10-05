<?php

class __Mustache_eaf3740dd1e4191cc592e2ffd97eb8eb extends Mustache_Template
{
    public function renderInternal(Mustache_Context $context, $indent = '')
    {
        $buffer = '';
        $newContext = array();

        $value = $this->resolveValue($context->find('body'), $context);
        $buffer .= $indent . $value;
        $buffer .= '
';

        return $buffer;
    }
}
